A = int(input())
B = int(input())
C = int(input())

result = str(A * B * C)

count = [0] * 10

for i in result:
    num = int(i)
    count[num] += 1

for i in range(10):
    print(count[i])