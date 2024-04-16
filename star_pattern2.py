#      *
#     **
#    ***
#   ****
#  *****
# ******

rows = int(input())  
i = 1 
while(i <= rows): 
    j = 1 
    while(j <= rows): 
        if(j <= rows - i): 
            print(' ', end = '  ') 
        else: 
            print('*', end = '  ') 
        j = j + 1 
    i = i + 1 
    print() 
