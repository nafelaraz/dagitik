import threading
import socket
import time
import random


class myThread (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        print "Starting " + self.name

        delay=random.random
        c.send('Thank you for connecting!')
        while True:
            #time.sleep(delay)
            #c.send('Merhaba saat su an',   time.ctime(time.time()) )

            #delay=random.random

            gelen = c.recv(1024)
            if gelen=="end":
                thread.join()
            else:
                print(gelen)
                c.send('peki')





threadID = 1
s = socket.socket() # Create a socket object
host = socket.gethostname() # Get local machine name
port = 1234 # Reserve a port for your service.
s.bind((host, port)) # Bind to the port

s.listen(5) # Now wait for client connection.

while True:
    c, addr = s.accept() # Establish connection with client.
    print "Yeni baglanti bekleniyor"
    print 'Got connection from', addr
    tName="thread"+str(threadID)
    thread = myThread(threadID, tName, 1)
    thread.start()

    threadID+=1



print "Exiting Main Thread"
