a,b=map(int,input().split())
c=2
lcm=1
while True:
    if a%c==0 and b%c==0:
        a=a//c
        b=b//c
        lcm=lcm*c
    else:
        c+=1
    if a<c or b<c:
        break
print(lcm*a*b)