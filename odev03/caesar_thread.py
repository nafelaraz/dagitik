



alfabe = 'abcdefghijklmnopqrstuvwxyz'
anahtar={}
s=input("kac harf saga kaydirilacagini giriniz :")
n=input("thread sayisini giriniz :")
l=input("blok uzunlugunu giriniz :")
isim="crypted_"+str(s)+"_"+ str(n)+"_"+str(l)+".txt"
print(isim)
dosya = open(isim,"w")

j=0

while j<26:

    anahtar[alfabe[j]]=alfabe[j-s]
    j+=1

print('alfabe=' , alfabe)
print('anahtar=' , anahtar)

#def sifrele():