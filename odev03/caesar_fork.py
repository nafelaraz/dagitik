from multiprocessing import Process, Lock



sayac=0

alfabe = 'abcdefghijklmnopqrstuvwxyz'
anahtar={}
s=input("kac harf saga kaydirilacagini giriniz :")
n=input("process sayisini giriniz :")
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

def sifrele():
    global sayac

    while sayac<=kac_karakter:
        Lock.acquire()
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
        Lock.release()



dosya=open("metin.txt","r")
dosya.read()
kac_karakter=dosya.tell()

Lock = Lock()
processes = []

k=0
# Create new process
while k<n:

    p = Process(target=sifrele)
    p.start()
    processes.append(p)
    p.join()
    k+=1


for t in processes:
    t.join()
print "Exiting "

