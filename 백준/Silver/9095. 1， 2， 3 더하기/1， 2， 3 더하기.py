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
    dp[4] = 7
    dp[5] = 13
    dp[6] = 24
    dp[7] = 44
    dp[8] = 81
    dp[9] = 149
    dp[10] = 274
    dp[11] = 504
    print(dp[a])