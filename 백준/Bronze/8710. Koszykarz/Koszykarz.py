a,b,c = map(int,input().split())
d = b -a

if d <= 0:
    print(0)
else:
    e = (d + c - 1)// c
    print(e)