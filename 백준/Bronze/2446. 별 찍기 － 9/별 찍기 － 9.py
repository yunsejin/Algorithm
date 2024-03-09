a = int(input())
for i in range(1,a+1):
    print(' '*(i-1)+'*'*((a-i+1)*2-1))
for i in range(a-1,0,-1):
    print(' '*(i-1)+'*'*((a-i+1)*2-1))