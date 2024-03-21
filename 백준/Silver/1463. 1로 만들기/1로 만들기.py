dp = [0] * (10**6+1)
dp[0] = 0
dp[1] = 0
dp[2] = 1
dp[3] = 1
dp[4] = 2
dp[5] = 3
dp[6] = 2
dp[7] = 3
dp[8] = 3
dp[9] = 2
dp[10] = 3
for i in range(11, 10**6+1):
    dp[i] = min(dp[i-1], dp[i//2] if i % 2 == 0 else 10**6, dp[i//3] if i % 3 == 0 else 10**6) + 1    
import sys
input = sys.stdin.readline
n = int(input())
print(dp[n])