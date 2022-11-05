i=int(input())
sum=0
sq=i*i
while sq!=0:
    rem=sq%10
    sum=sum+rem
    sq=sq//10
if i==sum:
    print("Neon Number")
else:
    print("Not Neon Number")