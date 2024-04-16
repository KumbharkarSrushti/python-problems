# Number Count in an Array:
# You are given an integer array. You are also given a number. Print the number of times the number appears in the array.
# Sample Input:
# 4 7 9 10 7 14 12 4 7 27
# 7
# Sample Output: 
# 3
# Explanation: The given number 7 appears 3 times in the given array.

a=[4, 7, 9, 10, 7, 14, 12, 4, 7, 27]
num=int(input())
count=0
for i in range(len(a)):
    if num==a[i]:
        count+=1
print(count)
