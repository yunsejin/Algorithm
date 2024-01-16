b = list(map(int, input().split()))
a = list(map(int, input().split()))


c = 0
d = 0


for i in range(9):
    c += b[i]
    if c > d:
        print('Yes')
        break
    d += a[i]
else:
    print('No')
