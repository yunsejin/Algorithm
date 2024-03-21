dp = [0] * (10**6+1)
dp[2] = 1
dp[3] = 1
for i in range(4, 10**6+1):
    dp[i] = min(dp[i-1], dp[i//2] if i % 2 == 0 else 10**6, dp[i//3] if i % 3 == 0 else 10**6) + 1    
import sys
input = sys.stdin.readline
n = int(input())
print(dp[n])