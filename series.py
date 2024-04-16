# Series: 3, 5, 7, 9, 11, …:
# You are given an integer n. Print first n terms of the series 3, 5, 7, 9, 11…
# Sample Input: 
# 7
# Sample Output: 
# 3 5 7 9 11 13 15
# Explanation: The series starts with 3 and every time adds 2 to get the next term.

n = 7
start = 3 
i = 0  
while i < n:
    series = start + i * 2
    print(series, end=" ")
    i += 1



# Series: 2, 5, 8, 11, 14, …:
# You are given an integer n. Print first n terms of the series 2, 5, 8, 11, 14…
# Sample Input: 
# 7
# Sample Output: 
# 2 5 8 11 14 17 20
# Explanation: The series starts with 2 and every time adds 3 to get the next term.

n = 7
start = 2
i = 0  
while i < n:
    series = start + i * 3
    print(series, end=" ")
    i += 1



# Series: 3, 6, 12, 24, 48, …:
# You are given an integer n. Print first n terms of the series 3, 6, 12, 24, 48…
# Sample Input: 
# 7
# Sample Output: 
# 3 6 12 24 48 96 192
# Explanation: The series starts with 3 and every time multiplies 2 to get the next term.

n = 7
start = 3  
multiplier = 2  
current_term = start 
for i in range(n):
    print(current_term, end=" ")
    current_term *= multiplier
