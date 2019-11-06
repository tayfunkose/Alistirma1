for i in range(1,1000):
    a=str(i)
    if int(a)<9:
        print(a,end=" ")

    if 9<int(a)<99:
        if int(a[0])+int(a[1])<9:
            print(a,end=" ")

    if int(a)>99:
        if int(a[0])+int(a[1])+int(a[2])<9:
            print(a,end=" ")
