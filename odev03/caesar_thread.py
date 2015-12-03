import threading

exitFlag = 0
sayac=0


alfabe = 'abcdefghijklmnopqrstuvwxyz'
anahtar={}
s=input("kac harf saga kaydirilacagini giriniz :")
n=input("thread sayisini giriniz :")
l=input("blok uzunlugunu giriniz :")
isim="crypted_"+str(s)+"_"+ str(n)+"_"+str(l)+".txt"
print(isim)
dosya = open(isim,"w")
dosya.close()
code=""
j=0

while j<26:

    anahtar[alfabe[j]]=alfabe[j-s].upper()
    code+=anahtar[alfabe[j]]
    j+=1

print('alfabe=' , alfabe)
print('anahtar=' , anahtar)
print('code=',code)

sifreli=[]


class myThread (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        print "Starting " + self.name
        print self.name + " sayac :" + str(sayac)

        sifrele()





def sifrele():
    global sayac
    global exitFlag
    while sayac<=kac_karakter:
        threadLock.acquire()
        oku=open("metin.txt","r")
        oku.seek(sayac)
        sayac+=l
        blok=oku.read(l)
        blok=blok.lower()
        

        i=0


        for i in blok:
            if i.isalpha():
                sifreli.append(anahtar[i])
                dosya=open(isim,"a")
                dosya.write(anahtar[i])
                dosya.close()

            else:
                dosya=open(isim,"a")
                dosya.write(i)
                dosya.close()
        threadLock.release()



dosya=open("metin.txt","r")
dosya.read()
kac_karakter=dosya.tell()

threadLock = threading.Lock()
threads = []
threadID = 1
k=0
# Create new threads
while k<n:
    tName="thread"+str(threadID)
    thread = myThread(threadID, tName, k)
    thread.start()
    threads.append(thread)
    threadID += 1
    k+=1


for t in threads:
    t.join()
print "Exiting Main Thread"

