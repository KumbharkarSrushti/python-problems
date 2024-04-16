a = [3, 5, 6, 2, 6, 4, 3, 2, 6, 3]
i = 0
d = []
s = []
y = []
max_count = 0
max_count_element = 0

while i < len(a):
    j = 0
    c = 0
    while j < len(a):
        if a[i] == a[j]:
            s.append(a[i])
            c += 1
        j += 1
    
    if a[i] not in d:
        d.append(a[i])

    if c > max_count:
        max_count = c
        max_count_element = a[i]
    
    i += 1

print("Element with maximum occurrence:", max_count_element)


