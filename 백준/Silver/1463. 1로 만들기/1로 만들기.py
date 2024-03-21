a = int(input())
dp = [0,0,0,0,0,0,0,0,0]
dp[1] = 0
dp[2] = 1
dp[3] = 1
i = 3
while i <= a:
    i += 1
    dp.append(0)
    dp[i] = min(dp[i-1], dp[i//2] if i % 2 == 0 else 10**6, dp[i//3] if i % 3 == 0 else 10**6) + 1    
print(dp[a])