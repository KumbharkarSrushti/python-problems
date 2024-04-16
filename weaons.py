# import math
# for _ in range(int(input())):
#     H, X, Y1, Y2, K= map(int, input().split())
#     laser_damage = 0
#     if math.ceil(H/Y1)<=K:
#         laser_damage+=math.ceil(H/Y1)
#     else:
#         laser_damage+=K+math.ceil((H-K*Y1)/Y2)

#     print(min(laser_damage, math.ceil(H/X)))