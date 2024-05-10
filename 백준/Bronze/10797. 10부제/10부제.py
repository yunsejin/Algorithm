a = int(input())
b = map(int,input().split())
g = 0
for i in b:
    if a == i:
        g += 1
print(g)