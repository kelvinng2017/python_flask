from flask import Flask, render_template, request, redirect, url_for, make_response, Response, jsonify
import json
import random as rand
import datetime
import win32com.client
import os
import pythoncom
import random as rand
from test_send_message import *
from function import *
from lxml import etree
app = Flask(__name__)
app.debug = True
timeNow = datetime.datetime.now()
Time = timeNow.strftime("%Y/%m/%d %H:%M:%S")
commandid = timeNow.strftime("%Y%m%d%H%M%S")+"" + \
    '{:0>4}'.format(rand.randint(1, 9999))
f = open('config.json', 'r')
data_json = json.load(f)
queue_info = win32com.client.Dispatch("MSMQ.MSMQQueueInfo")
user_id = ""+'{:0>4}'.format(rand.randint(1, 9999))
f = open('config.json', 'r')
data = json.load(f)
SendQueueName = data.get('SendQueueName', 'MESQueue')
RecvQueueName = data.get('RecvQueueName', 'ACSBridgeQueue')
ErrQueueName = data.get('ErrQueueName', 'MESQueue')
SendQueueIP = data.get('SendQueueIP', "tcp:192.168.0.90")
RecvQueueIP = data.get('RecvQueueIP', "tcp:192.168.0.85")
ErrQueueIP = data.get('ErrQueueIP', "tcp:192.168.0.91")
SendQueue = "direct=" + SendQueueIP + "\\PRIVATE$\\" + SendQueueName
RecvQueue = "direct=" + RecvQueueIP + "\\PRIVATE$\\" + RecvQueueName
ErrQueue = "direct=" + ErrQueueIP + "\\PRIVATE$\\" + ErrQueueName
HostName = os.getenv('COMPUTERNAME')
Version = '1.6'
PID = '00000000'
f.close()


def Response_headers(content):
    resp = Response(content)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp


def send_msmaq(label, message):
    queue_info.FormatName = SendQueue
    queue_send = None
    try:
        queue_send = queue_info.Open(2, 0)

        msg = win32com.client.Dispatch("MSMQ.MSMQMessage")
        msg.Label = label
        msg.Body = message

        msg.Send(queue_send)
        return "msmq has  send"
    except Exception as e:
        return "connect wrong"
    finally:
        queue_send.Close()
        print(SendQueue)


def recv_msmq():
    queue_info.FormatName = RecvQueue
    queue_receive = None
    try:
        queue_receive = queue_info.Open(1, 0)
        print("i am here recv2")
        timeout_sec = 5.0
        return_message = {}
        if queue_receive.Peek(pythoncom.Empty, pythoncom.Empty, timeout_sec * 1000):
            # log.logger.debug("server has send message to client")
            msg = queue_receive.Receive()
            return_message["message_label"] = (msg.Label).encode("utf-8")
            return_message["message_body"] = (msg.Body).encode("utf-8")
            queue_receive.Close()
            return return_message
        else:
            Time2 = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
            return_message["message_label"] = "msmq no label"
            return_message["message_body"] = "msmq no message"
            queue_receive.Close()
            return return_message
    except Exception as e:
        print("connect error")
        return_message["message_label"] = "connect wrong"
        return_message["message_Sbody"] = "connect wrong"
    finally:
        queue_receive.Close()


@app.route('/index', methods=['GET', 'POST'])
def index():
    function_list = ['STKMOVE', 'STKMOVE_R', '']

    if request.method == 'POST' and request.values['go_to'] == 'STKMOVE':
        # str1 = 'STKMOVE'
        # return render_template('index.html',function_list=function_list,str1=str1)
        return redirect(url_for('stkmove', strFunction=request.form.get('go_to')))
    if request.method == 'POST' and request.values['go_to'] == 'EQMOVE':
        str1 = 'EQMOVE'
        return render_template('index.html', function_list=function_list, str1=str1)

        # return redirect(url_for('index',str1=str1))
        """
        
        queue_info.FormatName = "direct=tcp:" + \
            "192.168.0.91"+"\\PRIVATE$\\"+"kelvinng"
        queue_send = None
        try:
            queue_send = queue_info.Open(2, 0)

            msg = win32com.client.Dispatch("MSMQ.MSMQMessage")
            msg.Label = "test_label"
            msg.Body = "test_message"

            msg.Send(queue_send)
            print("function send")
        except Exception as e:
            print("wrong")
        finally:
            queue_send.Close()
        """
        # return redirect(url_for('stkmove',strFunction=request.form.get('select_function')))
    # if request.method == 'POST' and request.values['go_to']=='page_three':
    #   return redirect(url_for('page_three'))
    return render_template('index.html', function_list=function_list)

    # return render_template('test_page.html')
testInfo = {}
need_change_to_input_list = ["OUTSTK", "LEAVE", "ARRIVE",
                             "VALIDINPUT", "OUTEQP", "INEQP", "CARR_ALARM", "INSTK", "FOUPINFO"]
check_need_to_send_function_list = [
    "STKMOVE", "EQMOVE", "EMPTYCARRMOVE", "CHANGECMD", "MOVEREQUEST", "INVDATA", "MOVESTATUSREQUEST"]
need_change_to_send_function_replay_list = [
    "OUTSTK_R", "LEAVE_R", "ARRIVE_R", "VALIDINPUT_R", "OUTEQP_R", "INEQP_R", "CARR_ALARM_R", "INSTK_R", "FOUPINFO_R"]


@app.route('/stkmove/<strFunction>', methods=['GET', 'POST'])
def stkmove(strFunction):
    strCARRIERRID_list = ["E002_stock1", "E003_stock1", "E004_stock1"]
    strTODEVICE_list = ["LSD002", "LSD003", "LSD004", "LSD005", "LSD022", "LSD023",
                        "LSD024", "LSD025", "LSD029", "LSD030", "LSD033",
                        "OCR01", "OCR02", "OCR03", "OCR04", "OCR05",
                        "WSD119", "WSD137", "WSD156", "WSD157", "WSD158", "WSD162", "WSD163", "WSD645"]
    stk_dict = {
        "strFunction": strFunction,
        "strCOMAND": commandid,
        "strFORNAME": "ACS",
        "strUSERID": user_id,
        "strCARRIERRID": strCARRIERRID_list,
        "strTODEVICE": strTODEVICE_list,
    }
    """
    if request.method == 'POST' and request.values['send_to_ACS_Getway']=='send_to_ACS_Getway':
        
        print("strCOMMANDID_value:"+(request.form.get('strCOMMANDID')).encode('utf-8'))
        print("strUSERID_value:"+(request.form.get('strUSERID')).encode('utf-8'))
        print("strCARRIERRID_value:"+(request.form.get('strCARRIERRID')).encode('utf-8'))
        print("strCARRIERTYPE_value:"+(request.form.get('strCARRIERTYPE')).encode('utf-8'))
        print("strFROMDEVICE_value:"+(request.form.get('strFROMDEVICE')).encode('utf-8'))
        print("strFROMPORT_value:"+(request.form.get('strFROMPORT')).encode('utf-8'))
        print("strTODEVICE_value:"+(request.form.get('strTODEVICE')).encode('utf-8'))
        print("strTOPORT_value:"+(request.form.get('strTOPORT')).encode('utf-8'))
        print("strEMPTYCARRIER_value:"+(request.form.get('strEMPTYCARRIER')).encode('utf-8'))
        print("strPRIORITY_value:"+(request.form.get('strPRIORITY')).encode('utf-8'))
        print("strMETHODNAME_value:"+(request.form.get('strMETHODNAME')).encode('utf-8'))
        print("strFORMNAME_value:"+(request.form.get('strFORMNAME')).encode('utf-8'))
        print("strCMD_value:"+(request.form.get('strCMD')).encode('utf-8'))
        
        print('function is send')
        stkmove_xml_data = STKMOVE.format(
            IP=SendQueueIP,
            QUEUE_NAME=SendQueueName,
            CLIENT_HOSTNAME=HostName,
            FUNCTION_VERSION=Version,
            PROCESS_ID=PID,
            TIMESTAMP=Time,
            COMMANDID=((request.form.get('strCOMMANDID')).encode('utf-8')),
            USERID=((request.form.get('strUSERID')).encode('utf-8')),
            CARRIERID=((request.form.get('strCARRIERRID')).encode('utf-8')),
            FROMDEVICE=((request.form.get('strFROMDEVICE')).encode('utf-8')),
            FROMPORT=((request.form.get('strFROMPORT')).encode('utf-8')),
            TODEVICE=((request.form.get('strTODEVICE')).encode('utf-8')),  
            TOPORT=((request.form.get('strTOPORT')).encode('utf-8')),
            EMPTYCARRIER=((request.form.get('strEMPTYCARRIER')).encode('utf-8')),
            PRIORITY=((request.form.get('strPRIORITY')).encode('utf-8')))
        print(stkmove_xml_data)
        testInfo['stkmove'] = stkmove_xml_data
        return json.dumps(testInfo)
        # return render_template('stkmove.html',xml_data=xml_data)
    """

    # send_message_host_mes(SendQueue,"test","test1")

    return render_template('stkmove.html', stk_dict=stk_dict)


@app.route('/send_function', methods=["GET", "POST"])
def send_function():
    print("i am here send")
    send_to_html_dict = {}
    send_method = (request.form.get('strMETHODNAME')).encode('utf-8')
    print(send_method)
    if(send_method == "STKMOVE"):
        print('stkmove function is send')
        STKMOVE_xml_data = STKMOVE.format(
            IP=SendQueueIP,
            QUEUE_NAME=SendQueueName,
            CLIENT_HOSTNAME=HostName,
            FUNCTION_VERSION=Version,
            PROCESS_ID=PID,
            TIMESTAMP=Time,
            COMMANDID=((request.form.get('strCOMMANDID')).encode('utf-8')),
            USERID=((request.form.get('strUSERID')).encode('utf-8')),
            CARRIERID=((request.form.get('strCARRIERRID')).encode('utf-8')),
            FROMDEVICE=((request.form.get('strFROMDEVICE')).encode('utf-8')),
            FROMPORT=((request.form.get('strFROMPORT')).encode('utf-8')),
            TODEVICE=((request.form.get('strTODEVICE')).encode('utf-8')),
            TOPORT=((request.form.get('strTOPORT')).encode('utf-8')),
            EMPTYCARRIER=(
                (request.form.get('strEMPTYCARRIER')).encode('utf-8')),
            PRIORITY=((request.form.get('strPRIORITY')).encode('utf-8')))
        print(STKMOVE_xml_data)
        status_of_send = send_msmaq(send_method, STKMOVE_xml_data)
        send_to_html_dict["status_of_send"] = status_of_send
        send_to_html_dict["send_xml"] = STKMOVE_xml_data
        if(send_to_html_dict["send_xml"][0] == "<"):
            root_send = etree.fromstring(send_to_html_dict["send_xml"])

            if(len(root_send[1]) > 1):
                if(len(root_send[1][-1]) >= 1):
                    if(root_send[1][-1][0].text in check_need_to_send_function_list):
                        if(str(root_send[1][-1][0].text) == "STKMOVE"):
                            send_to_html_dict["CLIENT_HOSTNAME"] = root_send[0][0].text
                            send_to_html_dict["FUNCTION"] = root_send[0][1].text
                            send_to_html_dict["SERVERNAME"] = root_send[0][2].text
                            send_to_html_dict["IP"] = root_send[0][3].text
                            send_to_html_dict["DLL_NAME"] = root_send[0][4].text
                            send_to_html_dict["FUNCTION_VERSION"] = root_send[0][5].text
                            send_to_html_dict["CLASSNAME"] = root_send[0][6].text
                            send_to_html_dict["PROCESS_ID"] = root_send[0][7].text
                            send_to_html_dict["QUEUE_NAME"] = root_send[0][8].text
                            send_to_html_dict["LANG"] = root_send[0][9].text
                            send_to_html_dict["TIMESTAMP"] = root_send[0][10].text
                            send_to_html_dict["strCOMMANDID"] = root_send[1][0].text
                            send_to_html_dict["strUSERID"] = root_send[1][1].text
                            send_to_html_dict["strCARRIERID"] = root_send[1][2].text
                            send_to_html_dict["strCARRIERIDTYPE"] = root_send[1][3].text
                            send_to_html_dict["strFROMDEVICE"] = root_send[1][4].text
                            send_to_html_dict["strFROMPORT"] = root_send[1][5].text
                            send_to_html_dict["strTODEVICE"] = root_send[1][6].text
                            send_to_html_dict["strTOPORT"] = root_send[1][7].text
                            send_to_html_dict["strEMPTYCARRIER"] = root_send[1][8].text
                            send_to_html_dict["strPRIORITY"] = root_send[1][9].text
                            send_to_html_dict["strMETHODNAME"] = root_send[1][-1][0].text
                            send_to_html_dict["strFORNAME"] = root_send[1][-1][1].text
                            send_to_html_dict["strCMD"] = root_send[1][-1][2].text
                            print(send_to_html_dict)

    else:
        send_to_html_dict["send_xml"] = "no this function"
    return jsonify(send_to_html_dict)


@app.route('/receive_function', methods=["GET", "POST"])
def receive_function_and_process_function():
    need_change_to_input_list = ["OUTSTK", "LEAVE", "ARRIVE",
                                 "VALIDINPUT", "OUTEQP", "INEQP", "CARR_ALARM", "INSTK", "FOUPINFO"]
    check_need_to_send_function_list = [
        "STKMOVE", "EQMOVE", "EMPTYCARRMOVE", "CHANGECMD", "MOVEREQUEST", "INVDATA", "MOVESTATUSREQUEST"]
    need_change_to_send_function_replay_list = [
        "OUTSTK_R", "LEAVE_R", "ARRIVE_R", "VALIDINPUT_R", "OUTEQP_R", "INEQP_R", "CARR_ALARM_R", "INSTK_R", "FOUPINFO_R"]
    print("i am here recv1")
    recv_dict = {}

    recv_msmq_dict = recv_msmq()
    recv_dict["message_label"] = recv_msmq_dict["message_label"]
    recv_dict["message_body"] = recv_msmq_dict["message_body"]
    return jsonify(recv_dict)


""""
@app.route('/page_two/<username>', methods=['GET', 'POST'])
def page_two(username):
    if request.method == 'POST' and request.values['go_to']=='index':
        # do stuff when the form is submitted

        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else
        
        return redirect(url_for('index'))
    if request.method == 'POST' and request.values['go_to']=='page_three':
        return redirect(url_for('page_three'))

    # show the form, it wasn't submitted
    return render_template('page_two.html',username=username)
@app.route('/page_three', methods=['GET', 'POST'])
def page_three():
    if request.method == 'POST' and request.values['go_to']=='index':
        # do stuff when the form is submitted

        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else
        return redirect(url_for('index'))
    if request.method == 'POST' and request.values['go_to']=='page_two':
        return redirect(url_for('page_two'))

    # show the form, it wasn't submitted
    return render_template('page_three.html')
"""
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8887, debug=True)
