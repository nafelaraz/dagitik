from multiprocessing import Process, Queue

sayac=0
q = Queue()

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
dosya=open("metin.txt","r")
dosya.read()
kac_karakter=dosya.tell()
dosya.close()

#Lock = Lock()
processes = []

sifreli=[]
sayi=0
while sayac<=kac_karakter:

    oku=open("metin.txt","r")
    oku.seek(sayac)
    sayac+=l
    q.put(oku.read(l))
    sayi+=1


def sifrele():

    for j in range(sayi):
        blok=q.get()
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



k=0
# Create new process
while k<n:

    p = Process(target=sifrele)
    p.start()
    processes.append(p)
    #p.join()
    k+=1


for t in processes:
    t.join()
print "Exiting "

