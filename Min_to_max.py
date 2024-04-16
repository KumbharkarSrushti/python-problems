t=int(input())
for i in range(t):
    N=int(input())
    A=list(map(int,input().split()))
    m=min(A)
    count=0
    for j in range(len(A)):
        if A[j]!=m:
            count=count+1 
    print(count)
