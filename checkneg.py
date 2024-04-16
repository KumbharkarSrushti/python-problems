a = list(map(int, input().split()))
has_negative = False
i = 0
while i < len(a):
    if a[i] < 0:
        has_negative = True
        break
    i += 1
if has_negative:
    print("yes")
else:
    print("no")
