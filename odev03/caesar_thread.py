



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
blok="nafel"
sifreli=[]
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


sifrele(blok)

#oku=open("metin.txt","r")
#
#
