import numpy

dizi1=numpy.random.normal(-3,1,1000)
dizi2=numpy.random.normal(0,1,1000)
histo1,histo2=[0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]

for i in dizi1:
    if i>=-20:
        if i <= 20:
            
            a=int(round(i))
            a+=20
            histo1[a]+=1.0
c=0
toplam1=sum(histo1)
print(toplam1,"toplam1")
while c<40:
    histo1[c]=histo1[c]/toplam1
    c+=1
            
for j in dizi2:
    if j>=-20:
        if j <= 20:
            
            b=int(round(j))
            b+=20
            
            histo2[b]+=1.0
d=0
toplam2=sum(histo2)
print(toplam2,"toplam2")
while d<40:
    histo2[d]=histo2[d]/toplam2
    d+=1                      
c=0
d=0
mesafe=0.0
for i in range(41):
    if histo1[i]==0.0:
        continue
    else:
        
    
        for j in range(41):
            if histo2[j]==0.0:
                continue
            else:

        
                    
                if histo1[i]>histo2[j]:
                    
                
                    histo1[i]-=histo2[j]
                    mesafe+=(histo2[j]*float(abs(i-j)))
                    histo2[j]=0.0
                    
            
                if histo2[j]>histo1[i]:
                    histo2[j]-=histo1[i]
                    mesafe+=(histo1[i]*float(abs(j-i)))
                    histo1[i]=0.0
                    
            
                if histo1[i]==histo2[j]:
                    mesafe+=(histo1[i]*float(abs(j-i)))
                    histo1[i]=0.0
                    histo2[j]=0.0
                    
                                                                                        
print(dizi1,dizi2)
print(histo1,histo2)
print("toplam mesafe=",mesafe)