n=int(input('enter a number of row you want to print?'))
i,j=0,0
for i in range(0,n):
    print()
    for j in range(0,i+1):
        print('*',end='')