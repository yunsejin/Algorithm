n = int(input())
c = list(map(int, input().split()))
c.sort()
b = 0
d = 0

for i in c:
    d += i
    b += d

print(b) 