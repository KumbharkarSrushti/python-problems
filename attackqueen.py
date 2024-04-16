T=int(input())
for _ in range(T):
    N,X,Y=map(int,input().split())
    count=0
    c=0
    count+=N-1
    c+=N-1
    for i in range(1,N):
        if 1<=X + i<=N and 1<=Y + i<=N:
            count+=1
        if 1<=X - i<=N and 1<=Y + i<=N:
            c+=1
        if 1<=X + i<=N and 1<=Y - i<=N:
            count+=1
        if 1<=X - i<=N and 1<=Y - i<=N:
            c+=1
    print(count+c)
        