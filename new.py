# N,L=map(int,input().split())
# A=list(map(int,input().split()))
# c=0
# for i in range(len(A)):
#     if A[i]>=L:
#         c=c+1
# print(c)


# M,D=map(int,input().split())
# y,m,d=map(int,input().split())
# if d>=1 and d<=30:
#     print(y,m,d)
# elif d>=31 and m>=12:
#     print(y+1,1,1)




# N, S, M, L = map(int, input().split())
# cost_per_egg_6 = S / 6
# cost_per_egg_8 = M / 8
# cost_per_egg_12 = L / 12
# min_cost_6 = cost_per_egg_6 * N
# min_cost_8 = cost_per_egg_8 * N
# min_cost_12 = cost_per_egg_12 * N
# min_cost = min(min_cost_6, min_cost_8, min_cost_12)
# print(int(min_cost))


# # Atcoder
# N, S, M, L = map(int, input().split())
# packs_6 = (N + 5) // 6  
# packs_8 = (N + 7) // 8  
# packs_12 = (N + 11) // 12 
# total_cost_6 = packs_6 * S
# total_cost_8 = packs_8 * M
# total_cost_12 = packs_12 * L
# min_cost = min(total_cost_6, total_cost_8, total_cost_12)
# print(min_cost)



T = int(input("Enter the number of test cases: "))
for _ in range(T):
    X = int(input())
    if X % 5 != 0:
        print(-1)
    count_5_rs = 0
    count_10_rs = 0
    count_10_rs = X // 10
    remaining_amount = X - (count_10_rs * 10)
    if remaining_amount % 5 == 0:
        count_5_rs = remaining_amount // 5
    else:
        print(-1)
    total_coins = count_5_rs + count_10_rs
    print(total_coins)


