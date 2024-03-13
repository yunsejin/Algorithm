n = int(input())
a = list(int(input()) for _ in range(n))
b = list(i for i in range(1, n+1))
s = []
r = []
while b:
    s.append(b.pop(0))
    r.append('+')
    while s and s[-1] == a[0]:
        s.pop()
        a.pop(0)
        r.append('-')
if s:
    print('NO')
else:
    for i in r:
        print(i)