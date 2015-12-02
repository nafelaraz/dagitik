



alfabe = 'abcdefghijklmnopqrstuvwxyz'
anahtar={}
s=input("kac harf saga kaydirilacagini giriniz :")

j=0

while j<26:

    anahtar[alfabe[j]]=alfabe[j-s]
    j+=1

print('alfabe=' , alfabe)
print('anahtar=' , anahtar)
