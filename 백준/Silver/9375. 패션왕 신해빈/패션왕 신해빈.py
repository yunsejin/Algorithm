n = int(input())
for i in range(n):
    m = int(input())
    a = {}
    for j in range(m):
        name, kind = input().split()
        if kind in a:
            a[kind] += 1
        else:
            a[kind] = 1
    ans = 1
    for k in a:
        ans *= (a[k] + 1)
    print(ans - 1)