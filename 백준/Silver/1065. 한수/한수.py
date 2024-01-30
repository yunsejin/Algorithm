a = int(input())
b = []
for i in range(1, a+1):
    b.append(i)
count = 0
for i in b:
    if i < 100:
        count += 1
    else:
        c = list(map(int, str(i)))
        if c[0] - c[1] == c[1] - c[2]:
            count += 1
print(count)