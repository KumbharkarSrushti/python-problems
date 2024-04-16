a=[10, 5, 6, 3, -1, 4, -3, 5, 6]
count=0
i=1
while i <len(a):
    count+=1
    if a[i]<0:
        break
    i=i+1
print(count)
