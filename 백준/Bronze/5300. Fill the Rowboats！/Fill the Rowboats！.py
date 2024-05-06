n = int(input())
pirates = []
for i in range(1, n + 1):
    pirates.append(str(i))
    if i % 6 == 0 or i == n:
        pirates.append("Go!")

print(" ".join(pirates))
