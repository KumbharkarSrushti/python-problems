num = int(input())
if num > 1:
    for i in range(2, num):
        if(num % i) == 0:
            print('No,Number is not Prime')
            break
    else:
        print('Yes,Number is Prime')
