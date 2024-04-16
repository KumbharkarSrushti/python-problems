T=int(input())
for _ in range(T):
    a=list(map(int,input().split()))
    sum = 0
    count = 0
    max_avrg = 0
    index = 0
    for i in a:
        sum += i
        count += 1
        average = sum / count
        if average > max_avrg:
            max_avrg = average
            index = i
    print(index)

