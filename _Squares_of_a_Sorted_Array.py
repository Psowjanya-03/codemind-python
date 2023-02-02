def insertionsort(n,arr):
    for i in range(n):
        temp=arr[i]
        j=i-1
        for j in range(i-1,-1,-1):
            if temp**2<arr[j]:
                arr[j+1]=arr[j]
            else:
                arr[j+1]=temp**2
                break
        else:
            arr[0]=temp**2

n=int(input())
arr=list(map(int,input().split()))
insertionsort(n,arr)
print(*arr)