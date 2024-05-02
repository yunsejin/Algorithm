a = int(input())
for i in range(a):
    b = input()
    c = list(b)
    d = []
    for i in c:
        if i.upper():
            d.append(i.lower())
    print(''.join(d))