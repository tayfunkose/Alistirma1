import math

def asalMi(n):
    for j in range(2,int(math.sqrt(n))+1):
        if n%j==0:
            return False
    return True

x=input("Bir sayi giriniz:")

if asalMi(int(x)):
    print("Bu sayi asal bir sayidir.")

else:
    print("Bu sayi asal bir sayi degildir.")
