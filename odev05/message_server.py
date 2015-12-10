import Queue
import threading




class WriteThread (threading.Thread):
    def __init__(self, name, cSocket, address, threadQueue, logQueue ):
        threading.Thread.__init__(self)
        self.name = name
        self.cSocket = cSocket
        self.address = address
        self.lQueue = logQueue
        self.tQueue = threadQueue
    def run(self):
        self.lQueue.put("Starting " + self.name)
        while True:
            queueLock.acquire()
            #...
            #...
            # burasi kuyrukta sirasi gelen mesajlari
            # gondermek icin kullanilacak
            if self.threadQueue.qsize() > 0:
                queue_message = self.threadQueue.get()
                # gonderilen ozel mesajsa
                if queue_message[0]:
                    message_to_send = "MSG " + queue_message[0] + queue_message[2]
                # genel mesajsa
                elif queue_message[1]:
                    message_to_send = "SAY " + queue_message[2]
                # hicbiri degilse sistem mesajidir
                else:
                    message_to_send = "SYS " + queue_message[2]
            self.csend(message_to_send)
            queueLock.release()
            #...
        self.lQueue.put("Exiting " + self.name)


class ReadThread (threading.Thread):
    def __init__(self, name, cSocket, address, logQueue):
        threading.Thread.__init__(self)
        self.name = name
        self.cSocket = cSocket
        self.address = address
        self.lQueue = logQueue
        self.fihrist = fihrist
        self.tQueue = threadQueue
    def parser(self, data):
        data = data.strip()
        # henuz login olmadiysa
        if not self.nickname and not data[0:3] == "USR":
            response = "ERL"
            self.csend(response)
            return 0
        # data sekli bozuksa
        if data[0:3] == "USR" and (data[4:].count(" "))>0 :
            response = "ERR"
            self.csend(response)
            return 0

        if data[0:3] == "USR":
            nickname = data[4:]
            if not self.fihrist.has_key(nickname):
                # kullanici yoksa
                response = "HEL " + nickname
                self.csend(response)
                queue=nickname+"Queue"
                self.fihrist[nickname]=queue
                # fihristi guncelle
                self.fihrist.update(self.fihrist)
                print(self.nickname+" has joined.")
                print("online members:",self.fihrist.keys()) #...
                self.lQueue.put(self.nickname + " has joined.")
                return 0
            else:
                # kullanici reddedilecek
                response = "REJ " + nickname
                self.csend(response)
                self.lQueue.put("Closing socket",self.cSocket.accept) #?
                # baglantiyi kapat
                self.cSocket.close()
                return 1
        elif data[0:3] == "QUI":
            response = "BYE " + self.nickname
            self.csend(response)
            #...
            # fihristten sil
            del self.fihrist[self.nickname]
            #...
            # log gonder
            self.lQueue.put(self.nickname + " has left.")
            # baglantiyi sil
            self.cSocket.close()
            #...
        elif data[0:3] == "LSQ":
            response = "LSA "+self.fihrist.keys()
            #...
            self.csend(response)
        elif data[0:3] == "TIC":
            response= "TOC"
            self.csend(response)
        elif data[0:3] == "SAY":
            response="SOK"
            self.csend(response)
        elif data[0:3] == "MSG":
            response="MOK"
            self.csend(response)
            #...
            if not to_nickname in self.fihrist.keys():
                response = "MNO"
            else:
                queue_message = (to_nickname, self.nickname, message)
                # gonderilecek threadQueueyu fihristten alip icine yaz
                self.fihrist[to_nickname].put(queue_message)
                response = "MOK"
            self.csend(response)
        else:
            # bir seye uymadiysa protokol hatasi verilecek
            response = "ERR"
            self.csend(response)
            #...
            #...

    def run(self):
        self.lQueue.put("Starting " + self.name)
        while True:
            incoming_data=self.cSocket.recv
            #...
            #...
            # burasi blocking bir recv halinde duracak
            # gelen protokol komutlari parserdan gecirilip
            # ilgili hareketler yapilacak
            #...
            #...
            queue_message = self.parser(incoming_data)
            #...
            #...
            # istemciye cevap h a z r l a .
            #...
            #...
            # cevap veya cevaplari gondermek zere
            # threadQueue'ya yaz
            # lock mekanizmasini unutma
            #...
            #...
        self.lQueue.put("Exiting " + self.name)

