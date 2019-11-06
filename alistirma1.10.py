sayac=0
for i in range(10000,100000):
    a=str(i)
    if a[0]+a[1]==a[3]+a[4]:
        sayac=sayac+1

print(sayac)
