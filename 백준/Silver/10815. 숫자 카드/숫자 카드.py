import sys
input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
a.sort()
c = []
for i in b:
    l, r = 0, n-1
    while l <= r:
        mid = (l+r)//2
        if a[mid] < i:
            l = mid + 1
        else:
            r = mid - 1
    if l < n and a[l] == i:
        c.append(1)
    else:
        c.append(0)
print(*c)