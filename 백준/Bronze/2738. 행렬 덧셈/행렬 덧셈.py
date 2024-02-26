n, m = map(int, input().split())
b = [list(map(int, input().split())) for _ in range(n)]
c = [list(map(int, input().split())) for _ in range(n)]
d = []
e = []
f = []
for i in b:
    for j in i:
        d.append(j)
for i in c:
    for j in i:
        e.append(j)
for i in range(n*m):
    f.append(d[i]+e[i])

g = [f[i * m:(i + 1) * m] for i in range(n)]

for row in g:
    print(' '.join(map(str, row)))