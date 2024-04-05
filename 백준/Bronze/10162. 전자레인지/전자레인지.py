a = int(input())
b = 0
c = 0
d = 0
if a % 10 != 0:
    print(-1)
else:
    b = a // 300
    a = a % 300
    c = a // 60
    a = a % 60
    d = a // 10
    print(b, c, d)