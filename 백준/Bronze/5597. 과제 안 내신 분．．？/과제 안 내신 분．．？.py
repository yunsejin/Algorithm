a = set(int(input()) for i in range(28))
b = []
for i in range(31):
    if i not in a:
        b.append(i)
b.sort()
print(b[-2])
print(b[-1])