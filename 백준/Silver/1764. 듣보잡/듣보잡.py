n, m = map(int, input().split())
a = set(input() for _ in range(n))
b = set(input() for _ in range(m))

c = a & b

print(len(c))
for i in sorted(c):
    print(i)