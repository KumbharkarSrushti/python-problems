B=int(input())
A=1
while A**A !=B:
    A=A+1
    if A > B:
        print(-1)
        break
print(A)



