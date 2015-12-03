



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
        sifreli.append(anahtar[blok[i]])
        i+=1
    print(sifreli)

sifrele(blok)

#oku=open("metin.txt","r")
#dosya=open(isim,"a")
#dosya.write(oku.read(blok))
