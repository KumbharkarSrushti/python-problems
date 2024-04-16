a=[10, 5, 6, 3, 0, 4, 3, 5, 6]
sum=0
i=0
while i<len(a):
    sum+=a[i]
    if a[i]==0:
        break
    i=i+1
print(sum)
    

