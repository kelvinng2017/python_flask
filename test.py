import imp
from test_send_message import *

f = open('config.json','r')
data_json = json.load(f)
SendQueueName = data_json.get('SendQueueName', 'ACSBridgeSendQueue')
SendQueueIP = data_json.get('SendQueueIP', "192.168.0.85")
SendQueue = "direct=" + SendQueueIP + "\\PRIVATE$\\" + SendQueueName
send_message_host_mes(SendQueue,"test1","test2")