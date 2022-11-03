n=int(input())
while n>9:
    l=0
    while n!=0:
        r=n%10
        n=n//10
        l+=r
    n=l
print(n)