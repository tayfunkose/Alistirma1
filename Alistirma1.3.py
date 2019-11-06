faktoriyel=1
toplam=1
for i in range(1,10000):
    faktoriyel=faktoriyel*i
    
    toplam=toplam+1/faktoriyel
    
print(toplam)
