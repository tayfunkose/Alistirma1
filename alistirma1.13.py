for i in range (10,100):
    for k in range(10,100):
        a=str(i)
        b=str(k)
        if int(a+b)==(i+k)*11:
            print(i,k)
