n, k = map(int, input().split())
cash = [int(input()) for i in range(n)]
count = 0
for i in cash[::-1]:
    count += k // i
    k %= i
print(count)