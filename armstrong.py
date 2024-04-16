n=int(input("enter the number"))
original=n
sum=0
while n>0:
    sum=sum+(n%10)*(n%10)*(n%10)
    n=n//10
if sum==original:
    print(original,"it is armstrong")
else:
    print("number is not armstrong")