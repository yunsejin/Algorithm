a = int(input())
b = list(map(int,input().split()))
c = int(input())
count = 0
for i in b:
    if i == c:
        count += 1
        
print(count)