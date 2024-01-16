array = []
n = int(input())
for i in range(n):
    array.append(int(input()))

array.sort()

print(*array, sep='\n')