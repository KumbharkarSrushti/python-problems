a =int(input())
b =int(input())
c =int(input())
if a <= b<= c:
    sorted_numbers = [a, b, c]
elif a <= c <= b:
    sorted_numbers = [a, c, b]
elif b <= a <= c:
    sorted_numbers = [b, a,c]
elif b <= c <= a:
    sorted_numbers = [b,c,a]
elif c <= a <= b:
    sorted_numbers = [c,a,b]
else: 
    sorted_numbers = [c,b,a]
print("Sorted Numbers:", sorted_numbers)
