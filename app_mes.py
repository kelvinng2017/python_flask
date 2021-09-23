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
        timeout_sec = 1.0
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
    function_list = ['STKMOVE', 'EQMOVE']

    if request.method == 'POST' and request.values['go_to'] == 'STKMOVE':
        # str1 = 'STKMOVE'
        # return render_template('index.html',function_list=function_list,str1=str1)
        return redirect(url_for('stkmove_new', strFunction=request.form.get('go_to')))
    if request.method == 'POST' and request.values['go_to'] == 'EQMOVE':
        str1 = 'EQMOVE'
        return redirect(url_for('eqmove', strFunction=request.form.get('go_to')))

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


@app.route('/stkmove_new/<strFunction>', methods=['GET', 'POST'])
def stkmove_new(strFunction):
    strCARRIERRID_list = ["ER-A01_stock1", "ER-B01_stock1"]
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

    # send_message_host_mes(SendQueue,"test","test1")

    return render_template('stkmove_new.html', stk_dict=stk_dict)


@app.route('/eqmove/<strFunction>', methods=['GET', 'POST'])
def eqmove(strFunction):
    strCARRIERRID_list = ["ER-A01_stock1", "ER-B01_stock1"]
    strFROMDEVICE_list = ["LSD002", "LSD003", "LSD004", "LSD005", "LSD022", "LSD023",
                          "LSD024", "LSD025", "LSD029", "LSD030", "LSD033",
                          "OCR01", "OCR02", "OCR03", "OCR04", "OCR05",
                          "WSD119", "WSD137", "WSD156", "WSD157", "WSD158", "WSD162", "WSD163", "WSD645"]
    stk_dict = {
        "strFunction": strFunction,
        "strCOMAND": commandid,
        "strFORNAME": "ACS",
        "strUSERID": user_id,
        "strCARRIERRID": strCARRIERRID_list,
        "strFROMDEVICE": strFROMDEVICE_list,
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

    return render_template('eqmove.html', stk_dict=stk_dict)


@app.route('/send_function', methods=["GET", "POST"])
def send_function():
    print("i am here send")
    send_dict = {}
    hope_dict = {
        "lunch": "burger",
    }
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
        status_of_send = send_msmaq(send_method, STKMOVE_xml_data)  # here
        send_dict["status_of_send"] = status_of_send
        send_dict["send_message_label"] = "STKMOVE"
        send_dict["send_message_body"] = STKMOVE_xml_data
        if(send_dict["send_message_body"][0] == "<"):
            root_send = etree.fromstring(send_dict["send_message_body"])
            if(len(root_send[1]) > 1):
                if(len(root_send[1][-1]) >= 1):
                    if(root_send[1][-1][0].text in check_need_to_send_function_list):
                        if(str(root_send[1][-1][0].text) == "STKMOVE"):
                            send_dict["sned_CLIENT_HOSTNAME"] = root_send[0][0].text
                            send_dict["sned_FUNCTION"] = root_send[0][1].text
                            send_dict["sned_SERVERNAME"] = root_send[0][2].text
                            send_dict["sned_IP"] = root_send[0][3].text
                            send_dict["sned_DLL_NAME"] = root_send[0][4].text
                            send_dict["sned_FUNCTION_VERSION"] = root_send[0][5].text
                            send_dict["sned_CLASSNAME"] = root_send[0][6].text
                            send_dict["sned_PROCESS_ID"] = root_send[0][7].text
                            send_dict["sned_QUEUE_NAME"] = root_send[0][8].text
                            send_dict["sned_LANG"] = root_send[0][9].text
                            send_dict["sned_TIMESTAMP"] = root_send[0][10].text
                            send_dict["sned_strCOMMANDID"] = root_send[1][0].text
                            send_dict["sned_strUSERID"] = root_send[1][1].text
                            send_dict["sned_strCARRIERID"] = root_send[1][2].text
                            send_dict["sned_strCARRIERIDTYPE"] = root_send[1][3].text
                            send_dict["sned_strFROMDEVICE"] = root_send[1][4].text
                            send_dict["sned_strFROMPORT"] = root_send[1][5].text
                            send_dict["sned_strTODEVICE"] = root_send[1][6].text
                            send_dict["sned_strTOPORT"] = root_send[1][7].text
                            send_dict["sned_strEMPTYCARRIER"] = root_send[1][8].text
                            send_dict["sned_strPRIORITY"] = root_send[1][9].text
                            send_dict["sned_strMETHODNAME"] = root_send[1][-1][0].text
                            send_dict["sned_strFORNAME"] = root_send[1][-1][1].text
                            send_dict["sned_strCMD"] = root_send[1][-1][2].text
                            return jsonify(send_dict)
    elif(send_method == "EQMOVE"):
        print("eqmove function is send")
        EQMOVE_xml_data = EQMOVE.format(
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
        print(EQMOVE_xml_data)
        status_of_send = send_msmaq(send_method, EQMOVE_xml_data)
        send_dict["status_of_send"] = status_of_send
        send_dict["send_message_label"] = "EQMOVE"
        send_dict["send_message_body"] = EQMOVE_xml_data
        if(send_dict["send_message_body"][0] == "<"):
            root_send = etree.fromstring(send_dict["send_message_body"])
            print("i am here11111111")
            if(len(root_send[1]) > 1):
                print("i am here2222222222222")
                if(len(root_send[1][-1]) >= 1):
                    print("i am here3333333333")
                    if(root_send[1][-1][0].text in check_need_to_send_function_list):
                        print("i am here44444444")
                        if(str(root_send[1][-1][0].text) == "EQMOVE"):
                            print("i am here")
                            send_dict["CLIENT_HOSTNAME"] = root_send[0][0].text
                            send_dict["FUNCTION"] = root_send[0][1].text
                            send_dict["SERVERNAME"] = root_send[0][2].text
                            send_dict["IP"] = root_send[0][3].text
                            send_dict["DLL_NAME"] = root_send[0][4].text
                            send_dict["FUNCTION_VERSION"] = root_send[0][5].text
                            send_dict["CLASSNAME"] = root_send[0][6].text
                            send_dict["PROCESS_ID"] = root_send[0][7].text
                            send_dict["QUEUE_NAME"] = root_send[0][8].text
                            send_dict["LANG"] = root_send[0][9].text
                            send_dict["TIMESTAMP"] = root_send[0][10].text
                            send_dict["strCOMMANDID"] = root_send[1][0].text
                            send_dict["strUSERID"] = root_send[1][1].text
                            send_dict["strCARRIERID"] = root_send[1][2].text
                            send_dict["strCARRIERIDTYPE"] = root_send[1][3].text
                            send_dict["strFROMDEVICE"] = root_send[1][4].text
                            send_dict["strFROMPORT"] = root_send[1][5].text
                            send_dict["strTODEVICE"] = root_send[1][6].text
                            send_dict["strTOPORT"] = root_send[1][7].text
                            send_dict["strEMPTYCARRIER"] = root_send[1][8].text
                            send_dict["strPRIORITY"] = root_send[1][9].text
                            send_dict["strMETHODNAME"] = root_send[1][-1][0].text
                            send_dict["strFORNAME"] = root_send[1][-1][1].text
                            send_dict["strCMD"] = root_send[1][-1][2].text
                            print(send_dict)
                            return jsonify(send_dict)
    else:
        send_dict["send_message_body"] = "no this function"
        return jsonify(send_dict)
    # return jsonify(send_dict)


@app.route('/receive_function', methods=["GET", "POST"])
def receive_function_and_process_function():
    hope_dict = {
        "lunch": "burger",
    }
    need_change_to_input_list = ["OUTSTK", "LEAVE", "ARRIVE",
                                 "VALIDINPUT", "OUTEQP", "INEQP", "CARR_ALARM", "INSTK", "FOUPINFO"]
    check_need_to_send_function_list = [
        "STKMOVE", "EQMOVE", "EMPTYCARRMOVE", "CHANGECMD", "MOVEREQUEST", "INVDATA", "MOVESTATUSREQUEST"]
    need_change_to_send_function_replay_list = [
        "OUTSTK_R", "LEAVE_R", "ARRIVE_R", "VALIDINPUT_R", "OUTEQP_R", "INEQP_R", "CARR_ALARM_R", "INSTK_R", "FOUPINFO_R"]
    print("i am here recv1")
    recv_dict = {}
    recv_dict_2 = {}
    send_dict = {}

    recv_msmq_dict = recv_msmq()

    recv_dict["recv_message_label"] = recv_msmq_dict["message_label"]
    recv_dict["recv_message_body"] = recv_msmq_dict["message_body"]
    if(recv_dict["recv_message_body"][0] == "<"):
        root_recv = etree.fromstring(recv_dict["recv_message_body"])
        if(len(root_recv) > 1):
            if(len(root_recv[1][-1]) >= 1):
                if(root_recv[1][-1][0].text not in need_change_to_input_list):
                    if(str(root_recv[1][-1][0].text) == "STKMOVE_R"):
                        recv_dict["recv_CLIENT_HOSTNAME"] = root_recv[0][0].text
                        recv_dict["recv_FUNCTION"] = root_recv[0][1].text
                        recv_dict["recv_SERVERNAME"] = root_recv[0][2].text
                        recv_dict["recv_IP"] = root_recv[0][3].text
                        recv_dict["recv_DLL_NAME"] = root_recv[0][4].text
                        recv_dict["recv_FUNCTION_VERSION"] = root_recv[0][5].text
                        recv_dict["recv_CLASSNAME"] = root_recv[0][6].text
                        recv_dict["recv_PID"] = root_recv[0][7].text
                        recv_dict["recv_PROCESS_ID"] = root_recv[0][8].text
                        recv_dict["recv_QUEUE_NAME"] = root_recv[0][9].text
                        recv_dict["recv_LANG"] = root_recv[0][10].text
                        recv_dict["recv_TIMESTAMP"] = root_recv[0][11].text
                        recv_dict["recv_strCOMMANDID"] = root_recv[1][0].text
                        recv_dict["recv_strRESULT"] = root_recv[1][1].text
                        recv_dict["recv_strERRORMESSAGE"] = root_recv[1][2].text
                        recv_dict["recv_strMETHODNAME"] = root_recv[1][-1][0].text
                        recv_dict["recv_strFORNAME"] = root_recv[1][-1][1].text
                        recv_dict["recv_strCMD"] = root_recv[1][-1][2].text
                        print("STKOMVE_R="+str(recv_dict))
                        return jsonify(recv_dict)
                    if(str(root_recv[1][-1][0].text) == "EQMOVE_R"):
                        recv_dict["recv_CLIENT_HOSTNAME"] = root_recv[0][0].text
                        recv_dict["recv_FUNCTION"] = root_recv[0][1].text
                        recv_dict["recv_SERVERNAME"] = root_recv[0][2].text
                        recv_dict["recv_IP"] = root_recv[0][3].text
                        recv_dict["recv_DLL_NAME"] = root_recv[0][4].text
                        recv_dict["recv_FUNCTION_VERSION"] = root_recv[0][5].text
                        recv_dict["recv_CLASSNAME"] = root_recv[0][6].text
                        recv_dict["recv_PID"] = root_recv[0][7].text
                        recv_dict["recv_PROCESS_ID"] = root_recv[0][8].text
                        recv_dict["recv_QUEUE_NAME"] = root_recv[0][9].text
                        recv_dict["recv_LANG"] = root_recv[0][10].text
                        recv_dict["recv_TIMESTAMP"] = root_recv[0][11].text
                        recv_dict["recv_strCOMMANDID"] = root_recv[1][0].text
                        recv_dict["recv_strRESULT"] = root_recv[1][1].text
                        recv_dict["recv_strERRORMESSAGE"] = root_recv[1][2].text
                        recv_dict["recv_strMETHODNAME"] = root_recv[1][-1][0].text
                        recv_dict["recv_strFORNAME"] = root_recv[1][-1][1].text
                        recv_dict["recv_strCMD"] = root_recv[1][-1][2].text

                        return jsonify(recv_dict)
                    if(str(root_recv[1][-1][0].text) == "EMPTYCARRMOVE_R"):
                        recv_dict["recv_CLIENT_HOSTNAME"] = root_recv[0][0].text
                        recv_dict["recv_FUNCTION"] = root_recv[0][1].text
                        recv_dict["recv_SERVERNAME"] = root_recv[0][2].text
                        recv_dict["recv_IP"] = root_recv[0][3].text
                        recv_dict["recv_DLL_NAME"] = root_recv[0][4].text
                        recv_dict["recv_FUNCTION_VERSION"] = root_recv[0][5].text
                        recv_dict["recv_CLASSNAME"] = root_recv[0][6].text
                        recv_dict["recv_PID"] = root_recv[0][7].text
                        recv_dict["recv_PROCESS_ID"] = root_recv[0][8].text
                        recv_dict["recv_QUEUE_NAME"] = root_recv[0][9].text
                        recv_dict["recv_LANG"] = root_recv[0][10].text
                        recv_dict["recv_TIMESTAMP"] = root_recv[0][11].text
                        recv_dict["recv_strCOMMANDID"] = root_recv[1][0].text
                        recv_dict["recv_strRESULT"] = root_recv[1][1].text
                        recv_dict["recv_strERRORMESSAGE"] = root_recv[1][2].text
                        recv_dict["recv_strCARRIERID"] = root_recv[1][3].text
                        recv_dict["recv_strCARRIERTYPE"] = root_recv[1][4].text
                        recv_dict["recv_strFROMDEVICE"] = root_recv[1][5].text
                        recv_dict["recv_strFROMPORT"] = root_recv[1][6].text
                        recv_dict["recv_strTODEVICE"] = root_recv[1][7].text
                        recv_dict["recv_strTOPORT"] = root_recv[1][8].text
                        recv_dict["recv_strMETHODNAME"] = root_recv[1][-1][0].text
                        recv_dict["recv_strFORNAME"] = root_recv[1][-1][1].text
                        recv_dict["recv_strCMD"] = root_recv[1][-1][2].text
                        return jsonify(recv_dict)
                    if(str(root_recv[1][-1][0].text) == "CHANGECMD_R"):
                        recv_dict["recv_CLIENT_HOSTNAME"] = root_recv[0][0].text
                        recv_dict["recv_FUNCTION"] = root_recv[0][1].text
                        recv_dict["recv_SERVERNAME"] = root_recv[0][2].text
                        recv_dict["recv_IP"] = root_recv[0][3].text
                        recv_dict["recv_DLL_NAME"] = root_recv[0][4].text
                        recv_dict["recv_FUNCTION_VERSION"] = root_recv[0][5].text
                        recv_dict["recv_CLASSNAME"] = root_recv[0][6].text
                        recv_dict["recv_PID"] = root_recv[0][7].text
                        recv_dict["recv_PROCESS_ID"] = root_recv[0][8].text
                        recv_dict["recv_QUEUE_NAME"] = root_recv[0][9].text
                        recv_dict["recv_LANG"] = root_recv[0][10].text
                        recv_dict["recv_TIMESTAMP"] = root_recv[0][11].text
                        recv_dict["recv_strCOMMANDID"] = root_recv[1][0].text
                        recv_dict["recv_strRESULT"] = root_recv[1][1].text
                        recv_dict["recv_strERRORMESSAGE"] = root_recv[1][2].text
                        recv_dict["recv_strMETHODNAME"] = root_recv[1][-1][0].text
                        recv_dict["recv_strFORNAME"] = root_recv[1][-1][1].text
                        recv_dict["recv_strCMD"] = root_recv[1][-1][2].text
                        return jsonify(recv_dict)
                    if(str(root_recv[1][-1][0].text) == "INVDATA_R"):
                        recv_dict["recv_CLIENT_HOSTNAME"] = root_recv[0][0].text
                        recv_dict["recv_FUNCTION"] = root_recv[0][1].text
                        recv_dict["recv_SERVERNAME"] = root_recv[0][2].text
                        recv_dict["recv_IP"] = root_recv[0][3].text
                        recv_dict["recv_DLL_NAME"] = root_recv[0][4].text
                        recv_dict["recv_FUNCTION_VERSION"] = root_recv[0][5].text
                        recv_dict["recv_CLASSNAME"] = root_recv[0][6].text
                        recv_dict["recv_PID"] = root_recv[0][7].text
                        recv_dict["recv_PROCESS_ID"] = root_recv[0][8].text
                        recv_dict["recv_QUEUE_NAME"] = root_recv[0][9].text
                        recv_dict["recv_LANG"] = root_recv[0][10].text
                        recv_dict["recv_TIMESTAMP"] = root_recv[0][11].text
                        recv_dict["recv_strCOMMANDID"] = root_recv[1][0].text
                        recv_dict["recv_strSTKID"] = root_recv[1][1].text
                        recv_dict["recv_strCOUNT"] = root_recv[1][2].text
                        recv_dict["recv_strCARRIERIDList"] = root_recv[1][3].text
                        recv_dict["recv_strSTKSTATUS"] = root_recv[1][4].text
                        recv_dict["recv_strRESULT"] = root_recv[1][5].text
                        recv_dict["recv_strERRORMESSAGE"] = root_recv[1][6].text
                        recv_dict["recv_strMETHODNAME"] = root_recv[1][-1][0].text
                        recv_dict["recv_strFORNAME"] = root_recv[1][-1][1].text
                        recv_dict["recv_strCMD"] = root_recv[1][-1][2].text
                        return jsonify(recv_dict)
                    if(str(root_recv[1][-1][0].text) == "MOVESTATUSREQUEST_R"):
                        recv_dict["recv_CLIENT_HOSTNAME"] = root_recv[0][0].text
                        recv_dict["recv_FUNCTION"] = root_recv[0][1].text
                        recv_dict["recv_SERVERNAME"] = root_recv[0][2].text
                        recv_dict["recv_IP"] = root_recv[0][3].text
                        recv_dict["recv_DLL_NAME"] = root_recv[0][4].text
                        recv_dict["recv_FUNCTION_VERSION"] = root_recv[0][5].text
                        recv_dict["recv_CLASSNAME"] = root_recv[0][6].text
                        recv_dict["recv_PID"] = root_recv[0][7].text
                        recv_dict["recv_PROCESS_ID"] = root_recv[0][8].text
                        recv_dict["recv_QUEUE_NAME"] = root_recv[0][9].text
                        recv_dict["recv_LANG"] = root_recv[0][10].text
                        recv_dict["recv_TIMESTAMP"] = root_recv[0][11].text
                        recv_dict["recv_strCOMMANDID"] = root_recv[1][0].text
                        recv_dict["recv_strCARRIERID"] = root_recv[1][1].text
                        recv_dict["recv_strMOVESTATUS"] = root_recv[1][2].text
                        recv_dict["recv_strTODEVICE"] = root_recv[1][3].text
                        recv_dict["recv_strTOPORT"] = root_recv[1][4].text
                        recv_dict["recv_strPRIORITY"] = root_recv[1][5].text
                        recv_dict["recv_strRESULT"] = root_recv[1][6].text
                        recv_dict["recv_strERRORMESSAGE"] = root_recv[1][7].text
                        recv_dict["recv_strMETHODNAME"] = root_recv[1][-1][0].text
                        recv_dict["recv_strFORNAME"] = root_recv[1][-1][1].text
                        recv_dict["recv_strCMD"] = root_recv[1][-1][2].text
                        return jsonify(recv_dict)
                if(root_recv[1][-1][0].text in need_change_to_input_list):
                    if(str(root_recv[1][-1][0].text) == "OUTSTK"):
                        recv_dict["recv_CLIENT_HOSTNAME"] = root_recv[0][0].text
                        recv_dict["recv_FUNCTION"] = root_recv[0][1].text
                        recv_dict["recv_SERVERNAME"] = root_recv[0][2].text
                        recv_dict["recv_IP"] = root_recv[0][3].text
                        recv_dict["recv_DLL_NAME"] = root_recv[0][4].text
                        recv_dict["recv_FUNCTION_VERSION"] = root_recv[0][5].text
                        recv_dict["recv_CLASSNAME"] = root_recv[0][6].text
                        recv_dict["recv_PROCESS_ID"] = root_recv[0][7].text
                        recv_dict["recv_QUEUE_NAME"] = root_recv[0][8].text
                        recv_dict["recv_LANG"] = root_recv[0][9].text
                        recv_dict["recv_TIMESTAMP"] = root_recv[0][10].text
                        recv_dict["recv_strCOMMANDID"] = root_recv[1][0].text
                        recv_dict["recv_strCARRIERID"] = root_recv[1][1].text
                        recv_dict["recv_strSTKID"] = root_recv[1][2].text
                        recv_dict["recv_strMETHODNAME"] = root_recv[1][-1][0].text
                        recv_dict["recv_strFORNAME"] = root_recv[1][-1][1].text
                        recv_dict["recv_strCMD"] = root_recv[1][-1][2].text
                        OUTSTK_R_xml_data = OUTSTK_R.format(
                            IP=recv_dict["recv_IP"],
                            QUEUE_NAME=recv_dict["recv_QUEUE_NAME"],
                            CLIENT_HOSTNAME=recv_dict["recv_CLIENT_HOSTNAME"],
                            FUNCTION_VERSION=recv_dict["recv_FUNCTION_VERSION"],
                            PROCESS_ID=recv_dict["recv_PROCESS_ID"],
                            TIMESTAMP=recv_dict["recv_TIMESTAMP"],
                            COMMANDID=recv_dict["recv_strCOMMANDID"],
                            RESULT="OK",
                            ERRORMESSAGE="")
                        print(OUTSTK_R_xml_data)
                        send_dict["send_message_body"] = OUTSTK_R_xml_data
                        send_dict["send_message_label"] = "OUTSTK_R"
                        send_msmaq(send_dict["send_message_label"],
                                   send_dict["send_message_body"])
                        if(send_dict["send_message_body"][0] == "<"):
                            root_send = etree.fromstring(
                                send_dict["send_message_body"])
                            if(len(root_send) > 1):
                                if(len(root_send[1][-1]) >= 1):
                                    if(root_send[1][-1][0].text in need_change_to_send_function_replay_list):
                                        if(str(root_send[1][-1][0].text) == "OUTSTK_R"):
                                            send_dict["send_CLIENT_HOSTNAME"] = root_send[0][0].text
                                            send_dict["send_FUNCTION"] = root_send[0][1].text
                                            send_dict["send_SERVERNAME"] = root_send[0][2].text
                                            send_dict["send_IP"] = root_send[0][3].text
                                            send_dict["send_DLL_NAME"] = root_send[0][4].text
                                            send_dict["send_FUNCTION_VERSION"] = root_send[0][5].text
                                            send_dict["send_CLASSNAME"] = root_send[0][6].text
                                            send_dict["send_PID"] = root_send[0][7].text
                                            send_dict["send_PROCESS_ID"] = root_send[0][8].text
                                            send_dict["send_QUEUE_NAME"] = root_send[0][9].text
                                            send_dict["send_LANG"] = root_send[0][10].text
                                            send_dict["send_TIMESTAMP"] = root_send[0][11].text
                                            send_dict["send_strCOMMANDID"] = root_send[1][0].text
                                            send_dict["send_strRESULT"] = root_send[1][1].text
                                            send_dict["send_strERRORMESSAGE"] = root_send[1][2].text
                                            send_dict["send_strMETHODNAME"] = root_send[1][-1][0].text
                                            send_dict["send_strFORNAME"] = root_send[1][-1][1].text
                                            send_dict["send_strCMD"] = root_send[1][-1][2].text
                        return jsonify(send_dict, recv_dict)
                    if(str(root_recv[1][-1][0].text) == "LEAVE"):
                        recv_dict["recv_CLIENT_HOSTNAME"] = root_recv[0][0].text
                        recv_dict["recv_FUNCTION"] = root_recv[0][1].text
                        recv_dict["recv_SERVERNAME"] = root_recv[0][2].text
                        recv_dict["recv_IP"] = root_recv[0][3].text
                        recv_dict["recv_DLL_NAME"] = root_recv[0][4].text
                        recv_dict["recv_FUNCTION_VERSION"] = root_recv[0][5].text
                        recv_dict["recv_CLASSNAME"] = root_recv[0][6].text
                        recv_dict["recv_PROCESS_ID"] = root_recv[0][7].text
                        recv_dict["recv_QUEUE_NAME"] = root_recv[0][8].text
                        recv_dict["recv_LANG"] = root_recv[0][9].text
                        recv_dict["recv_TIMESTAMP"] = root_recv[0][10].text
                        recv_dict["recv_strCOMMANDID"] = root_recv[1][0].text
                        recv_dict["recv_strCARRIERID"] = root_recv[1][1].text
                        recv_dict["recv_strVEHICLEID"] = root_recv[1][2].text
                        recv_dict["recv_strFROMDEVICE"] = root_recv[1][3].text
                        recv_dict["recv_strFROMPORT"] = root_recv[1][4].text
                        recv_dict["recv_strMETHODNAME"] = root_recv[1][-1][0].text
                        recv_dict["recv_strFORNAME"] = root_recv[1][-1][1].text
                        recv_dict["recv_strCMD"] = root_recv[1][-1][2].text
                        print("LEAVE:"+str(recv_dict))
                        # print(recv_dict_whit_xml)
                        LEAVE_R_xml_data = LEAVE_R.format(
                            IP=recv_dict["recv_IP"],
                            QUEUE_NAME=recv_dict["recv_QUEUE_NAME"],
                            CLIENT_HOSTNAME=recv_dict["recv_CLIENT_HOSTNAME"],
                            FUNCTION_VERSION=recv_dict["recv_FUNCTION_VERSION"],
                            PROCESS_ID=recv_dict["recv_PROCESS_ID"],
                            TIMESTAMP=recv_dict["recv_TIMESTAMP"],
                            COMMANDID=recv_dict["recv_strCOMMANDID"],
                            RESULT="OK",
                            ERRORMESSAGE="",

                        )
                        print(LEAVE_R_xml_data)
                        send_dict["send_message_body"] = LEAVE_R_xml_data
                        send_dict["send_message_label"] = "LEAVE_R"
                        send_msmaq(send_dict["send_message_label"],
                                   send_dict["send_message_body"])
                        if(send_dict["send_message_body"][0] == "<"):
                            print("check523")
                            root_send = etree.fromstring(
                                send_dict["send_message_body"])
                            if(len(root_send) > 1):
                                print("check529")
                                if(len(root_send[1][-1]) >= 1):
                                    print("check531")
                                    if(root_send[1][-1][0].text in need_change_to_send_function_replay_list):
                                        print("check533")
                                        if(str(root_send[1][-1][0].text) == "LEAVE_R"):
                                            print("check535")
                                            send_dict["send_CLIENT_HOSTNAME"] = root_send[0][0].text
                                            send_dict["send_FUNCTION"] = root_send[0][1].text
                                            send_dict["send_SERVERNAME"] = root_send[0][2].text
                                            send_dict["send_IP"] = root_send[0][3].text
                                            send_dict["send_DLL_NAME"] = root_send[0][4].text
                                            send_dict["send_FUNCTION_VERSION"] = root_send[0][5].text
                                            send_dict["send_CLASSNAME"] = root_send[0][6].text
                                            send_dict["send_PID"] = root_send[0][7].text
                                            send_dict["send_PROCESS_ID"] = root_send[0][8].text
                                            send_dict["send_QUEUE_NAME"] = root_send[0][9].text
                                            send_dict["send_LANG"] = root_send[0][10].text
                                            send_dict["send_TIMESTAMP"] = root_send[0][11].text
                                            send_dict["send_strCOMMANDID"] = root_send[1][0].text
                                            send_dict["send_strRESULT"] = root_send[1][1].text
                                            send_dict["send_strERRORMESSAGE"] = root_send[1][2].text
                                            send_dict["send_strMETHODNAME"] = root_send[1][-1][0].text
                                            send_dict["send_strFORNAME"] = root_send[1][-1][1].text
                                            send_dict["send_strCMD"] = root_send[1][-1][2].text
                                            print("LEAVE_R:"+str(send_dict))
                                            return jsonify(send_dict, recv_dict)
                    if(str(root_recv[1][-1][0].text) == "ARRIVE"):
                        recv_dict["recv_CLIENT_HOSTNAME"] = root_recv[0][0].text
                        recv_dict["recv_FUNCTION"] = root_recv[0][1].text
                        recv_dict["recv_SERVERNAME"] = root_recv[0][2].text
                        recv_dict["recv_IP"] = root_recv[0][3].text
                        recv_dict["recv_DLL_NAME"] = root_recv[0][4].text
                        recv_dict["recv_FUNCTION_VERSION"] = root_recv[0][5].text
                        recv_dict["recv_CLASSNAME"] = root_recv[0][6].text
                        recv_dict["recv_PROCESS_ID"] = root_recv[0][7].text
                        recv_dict["recv_QUEUE_NAME"] = root_recv[0][8].text
                        recv_dict["recv_LANG"] = root_recv[0][9].text
                        recv_dict["recv_TIMESTAMP"] = root_recv[0][10].text
                        recv_dict["recv_strCOMMANDID"] = root_recv[1][0].text
                        recv_dict["recv_strCARRIERID"] = root_recv[1][1].text
                        recv_dict["recv_strVEHICLEID"] = root_recv[1][2].text
                        recv_dict["recv_strTODEVICE"] = root_recv[1][3].text
                        recv_dict["recv_strTOPORT"] = root_recv[1][4].text
                        recv_dict["recv_strMETHODNAME"] = root_recv[1][-1][0].text
                        recv_dict["recv_strFORNAME"] = root_recv[1][-1][1].text
                        recv_dict["recv_strCMD"] = root_recv[1][-1][2].text
                        print(recv_dict)
                        # print(recv_dict_whit_xml)
                        ARRIVE_R_xml_data = ARRIVE_R.format(
                            IP=recv_dict["recv_IP"],
                            QUEUE_NAME=recv_dict["recv_QUEUE_NAME"],
                            CLIENT_HOSTNAME=recv_dict["recv_CLIENT_HOSTNAME"],
                            FUNCTION_VERSION=recv_dict["recv_FUNCTION_VERSION"],
                            PROCESS_ID=recv_dict["recv_PROCESS_ID"],
                            TIMESTAMP=recv_dict["recv_TIMESTAMP"],
                            COMMANDID=recv_dict["recv_strCOMMANDID"],
                            RESULT="OK",
                            ERRORMESSAGE="",

                        )
                        print(ARRIVE_R_xml_data)
                        send_dict["send_message_body"] = ARRIVE_R_xml_data
                        send_dict["send_message_label"] = "ARRIVE_R"
                        send_msmaq(send_dict["send_message_label"],
                                   send_dict["send_message_body"])
                        if(send_dict["send_message_body"][0] == "<"):
                            root_send = etree.fromstring(
                                send_dict["send_message_body"])
                            if(len(root_send) > 1):
                                if(len(root_send[1][-1]) >= 1):
                                    if(root_send[1][-1][0].text in need_change_to_send_function_replay_list):
                                        if(str(root_send[1][-1][0].text) == "ARRIVE_R"):
                                            send_dict["send_CLIENT_HOSTNAME"] = root_send[0][0].text
                                            send_dict["send_FUNCTION"] = root_send[0][1].text
                                            send_dict["send_SERVERNAME"] = root_send[0][2].text
                                            send_dict["send_IP"] = root_send[0][3].text
                                            send_dict["send_DLL_NAME"] = root_send[0][4].text
                                            send_dict["send_FUNCTION_VERSION"] = root_send[0][5].text
                                            send_dict["send_CLASSNAME"] = root_send[0][6].text
                                            send_dict["send_PID"] = root_send[0][7].text
                                            send_dict["send_PROCESS_ID"] = root_send[0][8].text
                                            send_dict["send_QUEUE_NAME"] = root_send[0][9].text
                                            send_dict["send_LANG"] = root_send[0][10].text
                                            send_dict["send_TIMESTAMP"] = root_send[0][11].text
                                            send_dict["send_strCOMMANDID"] = root_send[1][0].text
                                            send_dict["send_strRESULT"] = root_send[1][1].text
                                            send_dict["send_strERRORMESSAGE"] = root_send[1][2].text
                                            send_dict["send_strMETHODNAME"] = root_send[1][-1][0].text
                                            send_dict["send_strFORNAME"] = root_send[1][-1][1].text
                                            send_dict["send_strCMD"] = root_send[1][-1][2].text
                                            return jsonify(send_dict, recv_dict)
                    if(str(root_recv[1][-1][0].text) == "VALIDINPUT"):
                        recv_dict["recv_CLIENT_HOSTNAME"] = root_recv[0][0].text
                        recv_dict["recv_FUNCTION"] = root_recv[0][1].text
                        recv_dict["recv_SERVERNAME"] = root_recv[0][2].text
                        recv_dict["recv_IP"] = root_recv[0][3].text
                        recv_dict["recv_DLL_NAME"] = root_recv[0][4].text
                        recv_dict["recv_FUNCTION_VERSION"] = root_recv[0][5].text
                        recv_dict["recv_CLASSNAME"] = root_recv[0][6].text
                        recv_dict["recv_PROCESS_ID"] = root_recv[0][7].text
                        recv_dict["recv_QUEUE_NAME"] = root_recv[0][8].text
                        recv_dict["recv_LANG"] = root_recv[0][9].text
                        recv_dict["recv_TIMESTAMP"] = root_recv[0][10].text
                        recv_dict["recv_strCOMMANDID"] = root_recv[1][0].text
                        recv_dict["recv_strCARRIERID"] = root_recv[1][1].text
                        recv_dict["recv_strVEHICLEID"] = root_recv[1][2].text
                        recv_dict["recv_strACTIONTYPE"] = root_recv[1][3].text
                        recv_dict["recv_strFROMDEVICE"] = root_recv[1][4].text
                        recv_dict["recv_strFROMPORT"] = root_recv[1][5].text
                        recv_dict["recv_strTODEVICE"] = root_recv[1][6].text
                        recv_dict["recv_strTOPORT"] = root_recv[1][7].text
                        recv_dict["recv_strMETHODNAME"] = root_recv[1][-1][0].text
                        recv_dict["recv_strFORNAME"] = root_recv[1][-1][1].text
                        recv_dict["recv_strCMD"] = root_recv[1][-1][2].text
                        print(recv_dict)
                        # print(recv_dict_whit_xml)
                        VALIDINPUT_R_xml_data = VALIDINPUT_R.format(
                            IP=recv_dict["recv_IP"],
                            QUEUE_NAME=recv_dict["recv_QUEUE_NAME"],
                            CLIENT_HOSTNAME=recv_dict["recv_CLIENT_HOSTNAME"],
                            FUNCTION_VERSION=recv_dict["recv_FUNCTION_VERSION"],
                            PROCESS_ID=recv_dict["recv_PROCESS_ID"],
                            TIMESTAMP=recv_dict["recv_TIMESTAMP"],
                            COMMANDID=recv_dict["recv_strCOMMANDID"],
                            RESULT="OK",
                            ERRORMESSAGE="",

                        )
                        print(VALIDINPUT_R_xml_data)
                        send_dict["send_message_body"] = VALIDINPUT_R_xml_data
                        send_dict["send_message_label"] = "VALIDINPUT_R"
                        send_msmaq(send_dict["send_message_label"],
                                   send_dict["send_message_body"])
                        if(send_dict["send_message_body"][0] == "<"):
                            root_send = etree.fromstring(
                                send_dict["send_message_body"])
                            if(len(root_send) > 1):
                                if(len(root_send[1][-1]) >= 1):
                                    if(root_send[1][-1][0].text in need_change_to_send_function_replay_list):
                                        if(str(root_send[1][-1][0].text) == "VALIDINPUT_R"):
                                            send_dict["send_CLIENT_HOSTNAME"] = root_send[0][0].text
                                            send_dict["send_FUNCTION"] = root_send[0][1].text
                                            send_dict["send_SERVERNAME"] = root_send[0][2].text
                                            send_dict["send_IP"] = root_send[0][3].text
                                            send_dict["send_DLL_NAME"] = root_send[0][4].text
                                            send_dict["send_FUNCTION_VERSION"] = root_send[0][5].text
                                            send_dict["send_CLASSNAME"] = root_send[0][6].text
                                            send_dict["send_PID"] = root_send[0][7].text
                                            send_dict["send_PROCESS_ID"] = root_send[0][8].text
                                            send_dict["send_QUEUE_NAME"] = root_send[0][9].text
                                            send_dict["send_LANG"] = root_send[0][10].text
                                            send_dict["send_TIMESTAMP"] = root_send[0][11].text
                                            send_dict["send_strCOMMANDID"] = root_send[1][0].text
                                            send_dict["send_strRESULT"] = root_send[1][1].text
                                            send_dict["send_strERRORMESSAGE"] = root_send[1][2].text
                                            send_dict["send_strMETHODNAME"] = root_send[1][-1][0].text
                                            send_dict["send_strFORNAME"] = root_send[1][-1][1].text
                                            send_dict["send_strCMD"] = root_send[1][-1][2].text
                                            return jsonify(send_dict, recv_dict)
                    if(str(root_recv[1][-1][0].text) == "OUTEQP"):
                        recv_dict["recv_CLIENT_HOSTNAME"] = root_recv[0][0].text
                        recv_dict["recv_FUNCTION"] = root_recv[0][1].text
                        recv_dict["recv_SERVERNAME"] = root_recv[0][2].text
                        recv_dict["recv_IP"] = root_recv[0][3].text
                        recv_dict["recv_DLL_NAME"] = root_recv[0][4].text
                        recv_dict["recv_FUNCTION_VERSION"] = root_recv[0][5].text
                        recv_dict["recv_CLASSNAME"] = root_recv[0][6].text
                        recv_dict["recv_PROCESS_ID"] = root_recv[0][7].text
                        recv_dict["recv_QUEUE_NAME"] = root_recv[0][8].text
                        recv_dict["recv_LANG"] = root_recv[0][9].text
                        recv_dict["recv_TIMESTAMP"] = root_recv[0][10].text
                        recv_dict["recv_strCOMMANDID"] = root_recv[1][0].text
                        recv_dict["recv_strCARRIERID"] = root_recv[1][1].text
                        recv_dict["recv_strVEHICLEID"] = root_recv[1][2].text
                        recv_dict["recv_strFROMDEVICE"] = root_recv[1][3].text
                        recv_dict["recv_strFROMPORT"] = root_recv[1][4].text
                        recv_dict["recv_strMETHODNAME"] = root_recv[1][-1][0].text
                        recv_dict["recv_strFORNAME"] = root_recv[1][-1][1].text
                        recv_dict["recv_strCMD"] = root_recv[1][-1][2].text
                        print(recv_dict)
                        # print(recv_dict_whit_xml)
                        OUTEQP_R_xml_data = OUTEQP_R.format(
                            IP=recv_dict["recv_IP"],
                            QUEUE_NAME=recv_dict["recv_QUEUE_NAME"],
                            CLIENT_HOSTNAME=recv_dict["recv_CLIENT_HOSTNAME"],
                            FUNCTION_VERSION=recv_dict["recv_FUNCTION_VERSION"],
                            PROCESS_ID=recv_dict["recv_PROCESS_ID"],
                            TIMESTAMP=recv_dict["recv_TIMESTAMP"],
                            COMMANDID=recv_dict["recv_strCOMMANDID"],
                            RESULT="OK",
                            ERRORMESSAGE="",

                        )
                        print(OUTEQP_R_xml_data)
                        send_dict["send_message_body"] = OUTEQP_R_xml_data
                        send_dict["send_message_label"] = "OUTEQP_R"
                        send_msmaq(send_dict["send_message_label"],
                                   send_dict["send_message_body"])
                        if(send_dict["send_message_body"][0] == "<"):
                            root_send = etree.fromstring(
                                send_dict["send_message_body"])
                            if(len(root_send) > 1):
                                if(len(root_send[1][-1]) >= 1):
                                    if(root_send[1][-1][0].text in need_change_to_send_function_replay_list):
                                        if(str(root_send[1][-1][0].text) == "OUTEQP_R"):
                                            send_dict["send_CLIENT_HOSTNAME"] = root_send[0][0].text
                                            send_dict["send_FUNCTION"] = root_send[0][1].text
                                            send_dict["send_SERVERNAME"] = root_send[0][2].text
                                            send_dict["send_IP"] = root_send[0][3].text
                                            send_dict["send_DLL_NAME"] = root_send[0][4].text
                                            send_dict["send_FUNCTION_VERSION"] = root_send[0][5].text
                                            send_dict["send_CLASSNAME"] = root_send[0][6].text
                                            send_dict["send_PID"] = root_send[0][7].text
                                            send_dict["send_PROCESS_ID"] = root_send[0][8].text
                                            send_dict["send_QUEUE_NAME"] = root_send[0][9].text
                                            send_dict["send_LANG"] = root_send[0][10].text
                                            send_dict["send_TIMESTAMP"] = root_send[0][11].text
                                            send_dict["send_strCOMMANDID"] = root_send[1][0].text
                                            send_dict["send_strRESULT"] = root_send[1][1].text
                                            send_dict["send_strERRORMESSAGE"] = root_send[1][2].text
                                            send_dict["send_strMETHODNAME"] = root_send[1][-1][0].text
                                            send_dict["send_strFORNAME"] = root_send[1][-1][1].text
                                            send_dict["send_strCMD"] = root_send[1][-1][2].text
                                            return jsonify(send_dict, recv_dict)
                    if(str(root_recv[1][-1][0].text) == "INEQP"):
                        recv_dict["recv_CLIENT_HOSTNAME"] = root_recv[0][0].text
                        recv_dict["recv_FUNCTION"] = root_recv[0][1].text
                        recv_dict["recv_SERVERNAME"] = root_recv[0][2].text
                        recv_dict["recv_IP"] = root_recv[0][3].text
                        recv_dict["recv_DLL_NAME"] = root_recv[0][4].text
                        recv_dict["recv_FUNCTION_VERSION"] = root_recv[0][5].text
                        recv_dict["recv_CLASSNAME"] = root_recv[0][6].text
                        recv_dict["recv_PROCESS_ID"] = root_recv[0][7].text
                        recv_dict["recv_QUEUE_NAME"] = root_recv[0][8].text
                        recv_dict["recv_LANG"] = root_recv[0][9].text
                        recv_dict["recv_TIMESTAMP"] = root_recv[0][10].text
                        recv_dict["recv_strCOMMANDID"] = root_recv[1][0].text
                        recv_dict["recv_strCARRIERID"] = root_recv[1][1].text
                        recv_dict["recv_strVEHICLEID"] = root_recv[1][2].text
                        recv_dict["recv_strTODEVICE"] = root_recv[1][3].text
                        recv_dict["recv_strTOPORT"] = root_recv[1][4].text
                        recv_dict["recv_strMETHODNAME"] = root_recv[1][-1][0].text
                        recv_dict["recv_strFORNAME"] = root_recv[1][-1][1].text
                        recv_dict["recv_strCMD"] = root_recv[1][-1][2].text
                        print(recv_dict)
                        # print(recv_dict_whit_xml)
                        INEQP_R_xml_data = INEQP_R.format(
                            IP=recv_dict["recv_IP"],
                            QUEUE_NAME=recv_dict["recv_QUEUE_NAME"],
                            CLIENT_HOSTNAME=recv_dict["recv_CLIENT_HOSTNAME"],
                            FUNCTION_VERSION=recv_dict["recv_FUNCTION_VERSION"],
                            PROCESS_ID=recv_dict["recv_PROCESS_ID"],
                            TIMESTAMP=recv_dict["recv_TIMESTAMP"],
                            COMMANDID=recv_dict["recv_strCOMMANDID"],
                            RESULT="OK",
                            ERRORMESSAGE="",

                        )
                        print(INEQP_R_xml_data)
                        send_dict["send_message_body"] = INEQP_R_xml_data
                        send_dict["send_message_label"] = "INEQP_R"
                        send_msmaq(send_dict["send_message_label"],
                                   send_dict["send_message_body"])
                        if(send_dict["send_message_body"][0] == "<"):
                            print("check794")
                            root_send = etree.fromstring(
                                send_dict["send_message_body"])
                            if(len(root_send) > 1):
                                print("check798")
                                if(len(root_send[1][-1]) >= 1):
                                    print("check800")
                                    if(root_send[1][-1][0].text in need_change_to_send_function_replay_list):
                                        print("check802")
                                        if(str(root_send[1][-1][0].text) == "INEQP_R"):
                                            print("check804")
                                            send_dict["send_CLIENT_HOSTNAME"] = root_send[0][0].text
                                            send_dict["send_FUNCTION"] = root_send[0][1].text
                                            send_dict["send_SERVERNAME"] = root_send[0][2].text
                                            send_dict["send_IP"] = root_send[0][3].text
                                            send_dict["send_DLL_NAME"] = root_send[0][4].text
                                            send_dict["send_FUNCTION_VERSION"] = root_send[0][5].text
                                            send_dict["send_CLASSNAME"] = root_send[0][6].text
                                            send_dict["send_PID"] = root_send[0][7].text
                                            send_dict["send_PROCESS_ID"] = root_send[0][8].text
                                            send_dict["send_QUEUE_NAME"] = root_send[0][9].text
                                            send_dict["send_LANG"] = root_send[0][10].text
                                            send_dict["send_TIMESTAMP"] = root_send[0][11].text
                                            send_dict["send_strCOMMANDID"] = root_send[1][0].text
                                            send_dict["send_strRESULT"] = root_send[1][1].text
                                            send_dict["send_strERRORMESSAGE"] = root_send[1][2].text
                                            send_dict["send_strMETHODNAME"] = root_send[1][-1][0].text
                                            send_dict["send_strFORNAME"] = root_send[1][-1][1].text
                                            send_dict["send_strCMD"] = root_send[1][-1][2].text
                                            print("check823")
                                            return jsonify(send_dict, recv_dict)
                    if(str(root_recv[1][-1][0].text) == "CARR_ALARM"):
                        recv_dict["recv_CLIENT_HOSTNAME"] = root_recv[0][0].text
                        recv_dict["recv_FUNCTION"] = root_recv[0][1].text
                        recv_dict["recv_SERVERNAME"] = root_recv[0][2].text
                        recv_dict["recv_IP"] = root_recv[0][3].text
                        recv_dict["recv_DLL_NAME"] = root_recv[0][4].text
                        recv_dict["recv_FUNCTION_VERSION"] = root_recv[0][5].text
                        recv_dict["recv_CLASSNAME"] = root_recv[0][6].text
                        recv_dict["recv_PROCESS_ID"] = root_recv[0][7].text
                        recv_dict["recv_QUEUE_NAME"] = root_recv[0][8].text
                        recv_dict["recv_LANG"] = root_recv[0][9].text
                        recv_dict["recv_TIMESTAMP"] = root_recv[0][10].text
                        recv_dict["recv_strCOMMANDID"] = root_recv[1][0].text
                        recv_dict["recv_strCARRIERID"] = root_recv[1][1].text
                        recv_dict["recv_strVEHICLEID"] = root_recv[1][2].text
                        recv_dict["recv_strALARMCODE"] = root_recv[1][3].text
                        recv_dict["recv_strALARMDESC"] = root_recv[1][4].text
                        recv_dict["recv_strMETHODNAME"] = root_recv[1][-1][0].text
                        recv_dict["recv_strFORNAME"] = root_recv[1][-1][1].text
                        recv_dict["recv_strCMD"] = root_recv[1][-1][2].text
                        print(recv_dict)
                        # print(recv_dict_whit_xml)
                        CARR_ALARM_R_xml_data = CARR_ALARM_R.format(
                            IP=recv_dict["recv_IP"],
                            QUEUE_NAME=recv_dict["recv_QUEUE_NAME"],
                            CLIENT_HOSTNAME=recv_dict["recv_CLIENT_HOSTNAME"],
                            FUNCTION_VERSION=recv_dict["recv_FUNCTION_VERSION"],
                            PROCESS_ID=recv_dict["recv_PROCESS_ID"],
                            TIMESTAMP=recv_dict["recv_TIMESTAMP"],
                            COMMANDID=recv_dict["recv_strCOMMANDID"],
                            RESULT="OK",
                            ERRORMESSAGE="",

                        )
                        print(CARR_ALARM_R_xml_data)
                        send_dict["send_message_body"] = CARR_ALARM_R_xml_data
                        send_dict["send_message_label"] = "CARR_ALARM_R"
                        send_msmaq(send_dict["send_message_label"],
                                   send_dict["send_message_body"])
                        if(send_dict["send_message_body"][0] == "<"):
                            root_send = etree.fromstring(
                                send_dict["send_message_body"])
                            if(len(root_send) > 1):
                                if(len(root_send[1][-1]) >= 1):
                                    if(root_send[1][-1][0].text in need_change_to_send_function_replay_list):
                                        if(str(root_send[1][-1][0].text) == "CARR_ALARM_R"):
                                            send_dict["send_CLIENT_HOSTNAME"] = root_send[0][0].text
                                            send_dict["send_FUNCTION"] = root_send[0][1].text
                                            send_dict["send_SERVERNAME"] = root_send[0][2].text
                                            send_dict["send_IP"] = root_send[0][3].text
                                            send_dict["send_DLL_NAME"] = root_send[0][4].text
                                            send_dict["send_FUNCTION_VERSION"] = root_send[0][5].text
                                            send_dict["send_CLASSNAME"] = root_send[0][6].text
                                            send_dict["send_PID"] = root_send[0][7].text
                                            send_dict["send_PROCESS_ID"] = root_send[0][8].text
                                            send_dict["send_QUEUE_NAME"] = root_send[0][9].text
                                            send_dict["send_LANG"] = root_send[0][10].text
                                            send_dict["send_TIMESTAMP"] = root_send[0][11].text
                                            send_dict["send_strCOMMANDID"] = root_send[1][0].text
                                            send_dict["send_strRESULT"] = root_send[1][1].text
                                            send_dict["send_strERRORMESSAGE"] = root_send[1][2].text
                                            send_dict["send_strMETHODNAME"] = root_send[1][-1][0].text
                                            send_dict["send_strFORNAME"] = root_send[1][-1][1].text
                                            send_dict["send_strCMD"] = root_send[1][-1][2].text
                                            return jsonify(send_dict, recv_dict)
                    if(str(root_recv[1][-1][0].text) == "INSTK"):
                        recv_dict["recv_CLIENT_HOSTNAME"] = root_recv[0][0].text
                        recv_dict["recv_FUNCTION"] = root_recv[0][1].text
                        recv_dict["recv_SERVERNAME"] = root_recv[0][2].text
                        recv_dict["recv_IP"] = root_recv[0][3].text
                        recv_dict["recv_DLL_NAME"] = root_recv[0][4].text
                        recv_dict["recv_FUNCTION_VERSION"] = root_recv[0][5].text
                        recv_dict["recv_CLASSNAME"] = root_recv[0][6].text
                        recv_dict["recv_PROCESS_ID"] = root_recv[0][7].text
                        recv_dict["recv_QUEUE_NAME"] = root_recv[0][8].text
                        recv_dict["recv_LANG"] = root_recv[0][9].text
                        recv_dict["recv_TIMESTAMP"] = root_recv[0][10].text
                        recv_dict["recv_strCOMMANDID"] = root_recv[1][0].text
                        recv_dict["recv_strCARRIERID"] = root_recv[1][1].text
                        recv_dict["recv_strSTKID"] = root_recv[1][2].text
                        recv_dict["recv_strMETHODNAME"] = root_recv[1][-1][0].text
                        recv_dict["recv_strFORNAME"] = root_recv[1][-1][1].text
                        recv_dict["recv_strCMD"] = root_recv[1][-1][2].text
                        print(recv_dict)
                        # print(recv_dict_whit_xml)
                        INSTK_R_xml_data = INSTK_R.format(
                            IP=recv_dict["recv_IP"],
                            QUEUE_NAME=recv_dict["recv_QUEUE_NAME"],
                            CLIENT_HOSTNAME=recv_dict["recv_CLIENT_HOSTNAME"],
                            FUNCTION_VERSION=recv_dict["recv_FUNCTION_VERSION"],
                            PROCESS_ID=recv_dict["recv_PROCESS_ID"],
                            TIMESTAMP=recv_dict["recv_TIMESTAMP"],
                            COMMANDID=recv_dict["recv_strCOMMANDID"],
                            RESULT="OK",
                            ERRORMESSAGE="",

                        )
                        print(INSTK_R_xml_data)
                        send_dict["send_message_body"] = INSTK_R_xml_data
                        send_dict["send_message_label"] = "INSTK_R"
                        send_msmaq(send_dict["send_message_label"],
                                   send_dict["send_message_body"])
                        if(send_dict["send_message_body"][0] == "<"):
                            root_send = etree.fromstring(
                                send_dict["send_message_body"])
                            if(len(root_send) > 1):
                                if(len(root_send[1][-1]) >= 1):
                                    if(root_send[1][-1][0].text in need_change_to_send_function_replay_list):
                                        if(str(root_send[1][-1][0].text) == "INSTK_R"):
                                            send_dict["send_CLIENT_HOSTNAME"] = root_send[0][0].text
                                            send_dict["send_FUNCTION"] = root_send[0][1].text
                                            send_dict["send_SERVERNAME"] = root_send[0][2].text
                                            send_dict["send_IP"] = root_send[0][3].text
                                            send_dict["send_DLL_NAME"] = root_send[0][4].text
                                            send_dict["send_FUNCTION_VERSION"] = root_send[0][5].text
                                            send_dict["send_CLASSNAME"] = root_send[0][6].text
                                            send_dict["send_PID"] = root_send[0][7].text
                                            send_dict["send_PROCESS_ID"] = root_send[0][8].text
                                            send_dict["send_QUEUE_NAME"] = root_send[0][9].text
                                            send_dict["send_LANG"] = root_send[0][10].text
                                            send_dict["send_TIMESTAMP"] = root_send[0][11].text
                                            send_dict["send_strCOMMANDID"] = root_send[1][0].text
                                            send_dict["send_strRESULT"] = root_send[1][1].text
                                            send_dict["send_strERRORMESSAGE"] = root_send[1][2].text
                                            send_dict["send_strMETHODNAME"] = root_send[1][-1][0].text
                                            send_dict["send_strFORNAME"] = root_send[1][-1][1].text
                                            send_dict["send_strCMD"] = root_send[1][-1][2].text
                                            return jsonify(send_dict, recv_dict)
                    if(str(root_recv[1][-1][0].text) == "FOUPINFO"):
                        recv_dict["recv_CLIENT_HOSTNAME"] = root_recv[0][0].text
                        recv_dict["recv_FUNCTION"] = root_recv[0][1].text
                        recv_dict["recv_SERVERNAME"] = root_recv[0][2].text
                        recv_dict["recv_IP"] = root_recv[0][3].text
                        recv_dict["recv_DLL_NAME"] = root_recv[0][4].text
                        recv_dict["recv_FUNCTION_VERSION"] = root_recv[0][5].text
                        recv_dict["recv_CLASSNAME"] = root_recv[0][6].text
                        recv_dict["recv_PROCESS_ID"] = root_recv[0][7].text
                        recv_dict["recv_QUEUE_NAME"] = root_recv[0][8].text
                        recv_dict["recv_LANG"] = root_recv[0][9].text
                        recv_dict["recv_TIMESTAMP"] = root_recv[0][10].text
                        recv_dict["recv_strCOMMANDID"] = root_recv[1][0].text
                        recv_dict["recv_strCARRIERID"] = root_recv[1][1].text
                        recv_dict["recv_strMETHODNAME"] = root_recv[1][-1][0].text
                        recv_dict["recv_strFORNAME"] = root_recv[1][-1][1].text
                        recv_dict["recv_strCMD"] = root_recv[1][-1][2].text
                        print(recv_dict)
                        # print(recv_dict_whit_xml)
                        FOUPINFO_R_xml_data = FOUPINFO_R.format(
                            IP=recv_dict["recv_IP"],
                            QUEUE_NAME=recv_dict["recv_QUEUE_NAME"],
                            CLIENT_HOSTNAME=recv_dict["recv_CLIENT_HOSTNAME"],
                            FUNCTION_VERSION=recv_dict["recv_FUNCTION_VERSION"],
                            PROCESS_ID=recv_dict["recv_PROCESS_ID"],
                            TIMESTAMP=recv_dict["recv_TIMESTAMP"],
                            COMMANDID=recv_dict["recv_strCOMMANDID"],
                            CARRIERID=recv_dict["recv_strCARRIERID"],
                            TODEVICE="LSD023",
                            TOPORT="1234",
                            RESULT="OK",
                            ERRORMESSAGE="",

                        )
                        print(FOUPINFO_R_xml_data)
                        send_dict["send_message_body"] = FOUPINFO_R_xml_data
                        send_dict["send_message_label"] = "FOUPINFO_R"
                        send_msmaq(send_dict["send_message_label"],
                                   send_dict["send_message_body"])
                        if(send_dict["send_message_body"][0] == "<"):
                            root_send = etree.fromstring(
                                send_dict["send_message_body"])
                            if(len(root_send) > 1):
                                if(len(root_send[1][-1]) >= 1):
                                    if(root_send[1][-1][0].text in need_change_to_send_function_replay_list):
                                        if(str(root_send[1][-1][0].text) == "FOUPINFO_R"):
                                            send_dict["send_CLIENT_HOSTNAME"] = root_send[0][0].text
                                            send_dict["send_FUNCTION"] = root_send[0][1].text
                                            send_dict["send_SERVERNAME"] = root_send[0][2].text
                                            send_dict["send_IP"] = root_send[0][3].text
                                            send_dict["send_DLL_NAME"] = root_send[0][4].text
                                            send_dict["send_FUNCTION_VERSION"] = root_send[0][5].text
                                            send_dict["send_CLASSNAME"] = root_send[0][6].text
                                            send_dict["send_PID"] = root_send[0][7].text
                                            send_dict["send_PROCESS_ID"] = root_send[0][8].text
                                            send_dict["send_QUEUE_NAME"] = root_send[0][9].text
                                            send_dict["send_LANG"] = root_send[0][10].text
                                            send_dict["send_TIMESTAMP"] = root_send[0][11].text
                                            send_dict["send_strCOMMANDID"] = root_send[1][0].text
                                            send_dict["send_strCARRIERID"] = root_send[1][1].text
                                            send_dict["send_strTODEVICE"] = root_send[1][2].text
                                            send_dict["send_strTOPORT"] = root_send[1][3].text
                                            send_dict["send_strRESULT"] = root_send[1][4].text
                                            send_dict["send_strERRORMESSAGE"] = root_send[1][5].text
                                            send_dict["send_strMETHODNAME"] = root_send[1][-1][0].text
                                            send_dict["send_strFORNAME"] = root_send[1][-1][1].text
                                            send_dict["send_strCMD"] = root_send[1][-1][2].text
                                            return jsonify(send_dict, recv_dict)
                if(str(root_recv[1][1].tag) == "strALARMID"):
                    print(root_recv[1][1].tag)
                    recv_dict["recv_CLIENT_HOSTNAME"] = root_recv[0][0].text
                    recv_dict["recv_FUNCTION"] = root_recv[0][1].text
                    recv_dict["recv_SERVERNAME"] = root_recv[0][2].text
                    recv_dict["recv_IP"] = root_recv[0][3].text
                    recv_dict["recv_DLL_NAME"] = root_recv[0][4].text
                    recv_dict["recv_FUNCTION_VERSION"] = root_recv[0][5].text
                    recv_dict["recv_CLASSNAME"] = root_recv[0][6].text
                    recv_dict["recv_PROCESS_ID"] = root_recv[0][7].text
                    recv_dict["recv_QUEUE_NAME"] = root_recv[0][8].text
                    recv_dict["recv_LANG"] = root_recv[0][9].text
                    recv_dict["recv_TIMESTAMP"] = root_recv[0][10].text
                    recv_dict["recv_strEQCHAR"] = root_recv[1][0].text
                    recv_dict["recv_strALARMID"] = root_recv[1][1].text
                    recv_dict["recv_strEQPID"] = root_recv[1][2].text
                    recv_dict["recv_strALARMLEVEL"] = root_recv[1][3].text
                    recv_dict["recv_strALARMTYPE"] = root_recv[1][4].text
                    recv_dict["recv_strALARMCODE"] = root_recv[1][5].text
                    recv_dict["recv_strALARMMSG"] = root_recv[1][6].text
                    recv_dict["recv_strALARMSYS"] = root_recv[1][7].text
                    recv_dict["recv_strALARMSYS"] = root_recv[1][7].text
                    recv_dict["recv_strALARMTIME"] = root_recv[1][8].text
                    recv_dict["recv_strDEPT"] = root_recv[1][9].text
                    recv_dict["recv_strSTAGE"] = root_recv[1][10].text
                    return jsonify(send_dict, recv_dict)
    else:
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
