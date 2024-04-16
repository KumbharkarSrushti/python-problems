fac = int(input())
sum = 0
for i in range(1, fac):
    if fac % i == 0:
        sum += i
if sum== fac:
    print("Yes")
else:
    print("No")
