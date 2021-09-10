import json
class Bridge():
    def ReadConfig(self):
        f = open('config.json', 'r')
        data = json.load(f)
        self.SendQueueName = data.get('SendQueueName', 'ACSBridgeSendQueue')# no message use right
        self.RecvQueueName = data.get('RecvQueueName', 'ACSBridgeQueue')
        self.ErrQueueName = data.get('ErrQueueName', 'ACSBridgeErrQueue')
        self.SendQueueIP = data.get('SendQueueIP', "os:"+self.HostName)
        self.RecvQueueIP = data.get('RecvQueueIP', "os:"+self.HostName)
        self.ErrQueueIP = data.get('ErrQueueIP', "os:"+self.HostName)
        self.SendQueue = "direct=" + self.SendQueueIP + "\\PRIVATE$\\" + self.SendQueueName
        self.RecvQueue = "direct=" + self.RecvQueueIP + "\\PRIVATE$\\" + self.RecvQueueName
        self.ErrQueue = "direct=" + self.ErrQueueIP + "\\PRIVATE$\\" + self.ErrQueueName
        self.e82_ip = data.get('e82_ip', '192.168.56.101')
        self.e82_port = data.get('e82_port', 5000)
        self.e88_ip = data.get('e88_ip', '192.168.56.101')
        self.e88_port = data.get('e88_port', 5001)
        self.IP = data.get('IP', '127.0.0.1')
        self.STK_format = data.get('STK_format', "{Device}-{Port}")
        self.EQP_format = data.get('EQP_format', "{Device}")
        self.EmptyCarrier = data.get('EmptyCarrier', "No")
        self.STK_List = data.get('STK_List', {})

    
  


f = open('config.json', 'r')
data = json.load(f)
print(data.get('SendQueueName', 'ACSBridgeSendQueue'))