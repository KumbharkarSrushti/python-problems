n = int(input())
if n < 0:
    print("Factorial is not defined for negative numbers")
elif n == 0 or n == 1:
        print(1)    
else:
    factorial_result = 1
    for i in range(2, n + 1):
        factorial_result *= i
    print(factorial_result)