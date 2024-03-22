import sys
input = sys.stdin.readline
n = int(input())
for i in range(n):
    a = int(input())
    dp = [0] * (11+1)
    dp[0] = 0
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4
    if a > 3:
        for i in range(4, a+1):
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    print(dp[a])