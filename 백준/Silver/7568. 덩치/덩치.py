n = int(input())
s = []

for _ in range(n):
    w, h = map(int, input().split())
    s.append((w, h))

for i in s:
    rank = 1
    for j in s:
        if i[0] < j[0] and i[1] < j[1]:
                rank += 1
    print(rank, end = " ")