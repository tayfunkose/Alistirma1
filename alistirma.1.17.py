x=input("Lütfen 3 basamaklı veyahut 4 basamaklı bir sayi giriniz.")

while len(x)!=3 and len(x)!=4:
    print("Lutfen 3 veya 4 basamakli bir sayi giriniz.")
    x=input("Lütfen 3 basamaklı veyahut 4 basamaklı bir sayi giriniz.")

if len(x)==3:
   if x[0]==x[2]:
       print("Bu bir 3 basamakli palindromik sayidir.")
   else:
       print("Bu sayi palindromik sayi degildir.")

elif len(x)==4:
    if x[0]==x[3] and x[1]==x[2]:
        print("Bu bir 4 basamakli palindromik sayidir.")
    else:
        print("Bu sayi palindromik sayi degildir.")

