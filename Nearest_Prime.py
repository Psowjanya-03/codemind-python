t=int(input())
for i in range(t):
    n=int(input())
    a=n
    while 1:
        prime=True
        for i in range(2,int(a**0.5)+1):
            if a%i==0:
                prime=False
                break
        if prime==True:
            break
        else:
            a+=1
    b=n
    while 1:
        prime=True
        for i in range(2,int(a**0.5)+1):
            if b%i==0:
                prime=False
                break
        if prime==True:
            break
        else:
            b-=1
    if n-b<=a-n:
         print(b)
    else:
        print(a)