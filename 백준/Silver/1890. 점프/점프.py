n = int(input())
k = []

for i in range(n):
    k.append(list(map(int, input().split())))

dp = [[0 for _ in range(n)] for _ in range(n)]
dp[0][0] = 1
count = 0

for i in range(n):
    for j in range(n):
        if dp[i][j] == 0 or (i == n-1 and j == n-1):
            continue
        if i + k[i][j] < n:
            dp[i + k[i][j]][j] += dp[i][j]
        if j + k[i][j] < n:
            dp[i][j + k[i][j]] += dp[i][j]

print(dp[n-1][n-1])