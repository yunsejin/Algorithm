a = int(input())
for _ in range(a):
    n = int(input())
    c = list(map(int, input().split()))
    m = int(input())
    dp = [0] * (m+1)
    dp[0] = 1
    
    for money in c:
        for b in range(money, m+1):
            dp[b] += dp[b-money]

    print(dp[m])