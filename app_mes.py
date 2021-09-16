
from flask import Flask,render_template,request,redirect,url_for
import json
import random as rand
import datetime
import win32com.client
import os
import pythoncom
from test_send_message import *
app = Flask(__name__)
app.debug = True
timeNow = datetime.datetime.now()
commandid = timeNow.strftime("%Y%m%d%H%M%S")+""+'{:0>4}'.format(rand.randint(1, 9999))
f = open('config.json','r')
data_json = json.load(f)
queue_info = win32com.client.Dispatch("MSMQ.MSMQQueueInfo")




@app.route('/index',methods=['GET', 'POST'])
def index():
    function_list = ['STKMOVE','STKMOVE_R','']
    if request.method == 'POST' and request.values['send']=='send':
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
        return redirect(url_for('stkmove',strFunction=request.form.get('select_function')))
    #if request.method == 'POST' and request.values['go_to']=='page_three':
    #   return redirect(url_for('page_three'))
    return render_template('index.html',function_list=function_list)
@app.route('/stkmove/<strFunction>',methods=['GET','POST'])
def stkmove(strFunction):
    stk_dict = {
        "strCOMAND":commandid,
        "strFORNAME":"ACS",
    }
    
    if request.method == 'POST' and request.values['send_to_ACS_Getway']=='send_to_ACS_Getway':
        print("i am here",(request.form.get('strFORMNAME')).encode('utf-8'))
        print('function is send')
    
    #send_message_host_mes(SendQueue,"test","test1")

    return render_template('stkmove.html',strFunction=strFunction,stk_dict=stk_dict)
    
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
    app.run(host="192.168.0.85", port=8887, debug=True)

