n = int(input())
b = [float(input()) for i in range(n)]
b.sort()
for i in range(7):
    print(f'{b[i]:.3f}')