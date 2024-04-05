a = int(input())
b = input()
c = list(b)
d = []
e = 0
for i in range(len(c)):
    if c[i].isdigit():
        if i > 0 and c[i-1].isdigit():
            d[-1] = d[-1] * 10 + int(c[i])
        else:
            d.append(int(c[i]))
    elif d:
        e += sum(d)
        d = []
if d:
    e += sum(d)
print(e)