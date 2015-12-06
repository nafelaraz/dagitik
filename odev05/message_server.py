



def parser(self, data):
    data = data.strip()
    # henuz login olmadiysa
    if not self.nickname and not data[0:3] == "USR":
        response = "ERL"
        self.csend(response)
        return 0
    # data sekli bozuksa
    if data[0:3] == "USR" and (data[4:].count(" ")>0 or data[4:].count("ş")>0 or data[4:].count("ç")>0 or data[4:].count("ö")>0 or data[4:].count("ı")>0 or data[4:].count("ğ")>0 or data[4:].count("ü")>0) :
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
            self.lQueue.put("Closing socket",self.csoc.accept) #?
            # baglantiyi kapat
            self.csoc.close()
            return 1
    elif data[0:3] == "QUI":
        response = "BYE " + self.nickname
        self.csend(response)
        ...
        # fihristten sil
        del self.fihrist[self.nickname]
        ...
        # log gonder
        self.lQueue.put(self.nickname + " has left.")
        # baglantiyi sil
        ...
        ...
    elif data[0:3] == "LSQ":
        response = "LSA "+self.fihrist.keys()
        ...
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
        ...
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
        ...
        ...

