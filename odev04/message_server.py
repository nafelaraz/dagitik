import threading
import socket


class myThread (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        print "Starting " + self.name
        # Get lock to synchronize threads
        threadLock.acquire()
        s = socket.socket() # Create a socket object
        host = socket.gethostname() # Get local machine name
        port = 1234 # Reserve a port for your service.
        s.bind((host, port)) # Bind to the port

        s.listen(5) # Now wait for client connection.

        while True:
            global threadID
            c, addr = s.accept() # Establish connection with client.
            print 'Got connection from', addr
            c.send('Thank you for connecting!')
            tName="thread"+str(threadID)
            thread = myThread(threadID, tName, 1)
            thread.start()
            threads.append(thread)
            threadID+=1

        # Free lock to release next thread
        threadLock.release()


threadLock = threading.Lock()
threads = []
threadID = 1
tName="Main"
thread = myThread(threadID, tName, 1)
thread.start()
threads.append(thread)
threadID+=1

for t in threads:
    t.join()
print "Exiting Main Thread"
