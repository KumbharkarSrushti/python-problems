T = int(input()) 
for _ in range(T):
    A = list(map(int, input().split()))  
    min_val = A[0]  

    for num in A:
        if num < min_val:
            min_val = num  

    print(min_val) 
