n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
common_elements = []
i = 0
while i < len(A):
    j = 0
    while j < len(B):
        if A[i] == B[j] and A[i] not in common_elements:
            common_elements.append(A[i])
        j += 1
    i += 1
print(common_elements)
