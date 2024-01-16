a, b = map(int, input().split())
c = list(range(1, a+1))
d = []

while c:
    for _ in range(b-1):
        c.append(c.pop(0))
    d.append(c.pop(0))

print('<', end='')
print(*d, sep=', ', end='')
print('>')