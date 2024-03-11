a = list(input())
b = []
c = []
for i in range(len(a)//2):
    b += a[i]
for i in range(len(a)//2, len(a)):
    c += a[i]
if sum(map(int, b)) == sum(map(int, c)):
    print("LUCKY")
else:
    print("READY")