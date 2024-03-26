a, b = map(int, input().split())
s = [int(x) for x in input().split()]

s.sort()

box = []

def backt(x ,p):
    if len(p) == b:
        print(' '.join(map(str, p)))
        return
    for i in range(x, a):
        backt(i, p + [s[i]])

backt(0, [])