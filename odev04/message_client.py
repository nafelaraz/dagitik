import threading
import socket
class readThread (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        print "Starting " + self.name
        while true:
            gelen = c.recv()
            print(gelen)


class writeThread (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        print "Starting " + self.name

        s.send('Thank you for connecting!')
        while true:
            message=raw_input("mesaji giriniz:")
            s.send(message)


        if message=="end":
            self.name.join()



threadID = 1
s = socket.socket()
host = "127.0.0.1"
port = 1234
s.connect((host,port))

rThread = readThread(1,read,1)
rThread.start()
wThread = writeThread(2,write,2)
wThread.start()

