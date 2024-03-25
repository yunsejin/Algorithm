a, b = map(int, input().split())
s = [int(x) for x in input().split()]

s.sort()

box = []

def backt(x):
    if x == b:
        print(' '.join(map(str, box)))
        return
    for i in range(a):
        if s[i] in box:
            continue
        box.append(s[i])
        backt(x + 1)
        box.pop()

backt(0)