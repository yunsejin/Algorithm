def min_cost_to_paint_houses(costs):
    n = len(costs)
    
    dp = [[0] * 3 for _ in range(n)]
    
    dp[0][0] = costs[0][0]
    dp[0][1] = costs[0][1]
    dp[0][2] = costs[0][2]
    
    for i in range(1, n):
        dp[i][0] = costs[i][0] + min(dp[i-1][1], dp[i-1][2])
        dp[i][1] = costs[i][1] + min(dp[i-1][0], dp[i-1][2])
        dp[i][2] = costs[i][2] + min(dp[i-1][0], dp[i-1][1])
    
    return min(dp[n-1][0], dp[n-1][1], dp[n-1][2])

N = int(input())
costs = [list(map(int, input().split())) for _ in range(N)]

result = min_cost_to_paint_houses(costs)
print(result)
