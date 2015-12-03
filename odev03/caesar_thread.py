import threading

exitFlag = 0

alfabe = 'abcdefghijklmnopqrstuvwxyz'
anahtar={}
s=input("kac harf saga kaydirilacagini giriniz :")
n=input("thread sayisini giriniz :")
l=input("blok uzunlugunu giriniz :")
isim="crypted_"+str(s)+"_"+ str(n)+"_"+str(l)+".txt"
print(isim)
dosya = open(isim,"w")
dosya.close()

j=0

while j<26:

    anahtar[alfabe[j]]=alfabe[j-s]
    j+=1

print('alfabe=' , alfabe)
print('anahtar=' , anahtar)

sifreli=[]

class myThread (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        print "Starting " + self.name
        exitFlag = 0
        while not exitFlag:

            # Get lock to synchronize threads
            threadLock.acquire()
            oku=open("metin.txt","r")
            blok=oku.read(l)
            if blok:
                sifrele(blok)
            else:
                exitFlag=1

            # Free lock to release next thread
            threadLock.release()
def sifrele(blok):
    i=0
    while i<l:
        if blok[i]==" ":
            dosya=open(isim,"a")
            dosya.write(" ")
            i+=1
        elif blok[i]==".":
            dosya=open(isim,"a")
            dosya.write(".")
            i+=1
        elif blok[i]==":":
            dosya=open(isim,"a")
            dosya.write(":")
            i+=1
        elif blok[i]==";":
            dosya=open(isim,"a")
            dosya.write(";")
            i+=1
        elif blok[i]=="!":
            dosya=open(isim,"a")
            dosya.write("!")
            i+=1
        elif blok[i]==",":
            dosya=open(isim,"a")
            dosya.write(",")
            i+=1
        else:
            sifreli.append(anahtar[blok[i]])
            dosya=open(isim,"a")
            dosya.write(sifreli[i])
            i+=1
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

