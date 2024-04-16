T=int(input())
for _ in range(T):
    N=int(input())
    S=input()
    for i in range(N):
        if S[i]=="1" and S[i+1]=="00":
            print("YES")
        else:
            print("no")
