a, b = map(int, input().split())
if a < 0:
    a = -a
if b < 0:
    b = -b
while b != 0:
    temp = b
    b = a % b
    a = temp
print(a)
