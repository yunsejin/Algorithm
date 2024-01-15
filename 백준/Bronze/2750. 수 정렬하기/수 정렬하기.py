A = int(input())
a = []
for _ in range(A):
    b=int(input())
    a.append(b)

a.sort()
for num in a:
    print(num)