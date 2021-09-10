import json
import win32com.client
import pythoncom
pythoncom.CoInitialize()
f = open('config.json','r')
data_json = json.load(f)
SendQueueName = data_json.get('SendQueueName', 'ACSBridgeSendQueue')
SendQueueIP = data_json.get('SendQueueIP', "192.168.0.85")
SendQueue = "direct=" + SendQueueIP + "\\PRIVATE$\\" + SendQueueName

print(SendQueueName)
print(SendQueueIP)
print(SendQueue)


def send_message_host_mes(queue_name, label, message):
    """send message function"""
    # queue_info.FormatName = f"direct=os:{computer_name}\\PRIVATE$\\{queue_name}"
    
    #queue_info.FormatName = "direct=os:"+computer_name+"\\PRIVATE$\\"+queue_name
    queue_info = win32com.client.Dispatch("MSMQ.MSMQQueueInfo")
    
    queue_info.FormatName = queue_name
    queue_send = None

    try:
        queue_send = queue_info.Open(2, 0)

        msg = win32com.client.Dispatch("MSMQ.MSMQMessage")
        msg.Label = label
        msg.Body = message

        msg.Send(queue_send)

    except Exception as e:
        print("wrong")
    finally:
        queue_send.Close()
    
def show_why(number):
    print("why also me:",number)