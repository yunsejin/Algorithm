n = int(input())
b = []
for _ in range(n):
    w = list(map(int, input().split()))
    b.append(w)
b.sort(key=lambda x: (x[1], x[0]))
for j in b:
    print(' '.join(map(str, j)))
