a = [10,5,10, 3, 4, 3, 5, 6]
i = 0
while i < len(a):
    j = 0
    c = 0
    while j < len(a):
        if a[i] == a[j]:
            c += 1
        j += 1
    if c > 1:
        print(a[i])
        break
    i += 1

