a=[10, 5, 6, 3, 4, 3, 5, 6]
i=0
max=a[i]
min=a[i]
while i<len(a):
    if a[i]<min:
        min=a[i]
    i+=1
print("minimum number",min)