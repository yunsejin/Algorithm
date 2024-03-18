n = int(input())
dp = [0] * 101
dp[1] = 1
dp[2] = 1
dp[3] = 1
dp[4] = 2
dp[5] = 2
dp[6] = 3
dp[7] = 4
dp[8] = 5
dp[9] = 7
dp[10] = 9
for i in range(n):
    a = int(input())
    for j in range(11, a+1):
        dp[j] = dp[j-1] + dp[j-5]
    print(dp[a])