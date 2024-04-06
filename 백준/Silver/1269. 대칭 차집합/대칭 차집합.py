import sys
input = sys.stdin.readline
n = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = set(a)
d = set(b)
e = c - d
f = d - c
print(len(e) + len(f))