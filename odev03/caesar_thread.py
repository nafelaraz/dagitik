


alfabe = 'abcdefghijklmnopqrstuvwxyz'
anahtar={}

j=0

while j<26:

    anahtar[alfabe[j]]=alfabe[j-3]
    j+=1

print('alfabe=' , alfabe)
print('anahtar=' , anahtar)
