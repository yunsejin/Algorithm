import sys
input=sys.stdin.readline

a, b, c = map(int,input().split())
d = a - b
e = (c - b) // d

if (c - b) % d > 0:
    e += 1

print(e)