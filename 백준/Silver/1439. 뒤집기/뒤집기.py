a = list(input())
b = []
c = []
d = a.pop(0)

while a:
    e = a.pop(0)
    if d[-1] == e:
        d += e
    elif d[-1] != e and e == '1':
        b.append(d)
        d = e
    elif d[-1] != e and e == '0':
        c.append(d)
        d = e

if d[-1] == '0':
    b.append(d)
else:
    c.append(d)
print(min(len(b), len(c)))