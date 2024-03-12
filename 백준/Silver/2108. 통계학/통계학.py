import sys
input = sys.stdin.readline
a = int(input())
b = list(int(input()) for i in range(a))
print(round(sum(b) / a))
b.sort()
print(b[len(b) // 2])
c = {}
for i in b:
    if i in c:
        c[i] += 1
    else:
        c[i] = 1
d = sorted(c.items(), key=lambda x: (-x[1], x[0]))
if len(b) > 1:
    if d[0][1] == d[1][1]:
        print(d[1][0])
    else:
        print(d[0][0])
else:
    print(b[0])
print(abs(b[0] - b[-1]))