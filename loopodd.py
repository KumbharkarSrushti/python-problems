n = int(input("Enter the value of n: "))
odd = 0
odd_num = 1
while odd < n:
    if odd_num % 2 != 0:
        print(odd_num, end=" ")
        odd += 1
    odd_num += 1
