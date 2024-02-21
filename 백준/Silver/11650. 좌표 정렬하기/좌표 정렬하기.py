n = int(input())
c = []
d = []
for i in range(n):
    a, b = map(int,input().split())
    c.append(a)
    c.append(b)
    d.append(c[:])
    c.pop()
    c.pop()
d.sort(key=lambda x: (x[0], x[1]))
for j in d:
    print(' '.join(map(str, j)))