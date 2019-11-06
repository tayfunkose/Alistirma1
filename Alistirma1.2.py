import math
toplam=0
for i in range(1,100000):
    toplam=toplam+1/(i*i)

    
print(math.sqrt(6*toplam))
