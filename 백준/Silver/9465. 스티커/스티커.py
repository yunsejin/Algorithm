def max_sticker_score(test_cases):
    results = []
    
    for stickers in test_cases:
        n = len(stickers[0])
        if n == 1:
            results.append(max(stickers[0][0], stickers[1][0]))
            continue
        
        dp = [[0] * 3 for _ in range(n)]
        
        dp[0][0] = stickers[0][0]
        dp[0][1] = stickers[1][0]
        dp[0][2] = 0
        
        for i in range(1, n):
            dp[i][0] = max(dp[i-1][1], dp[i-1][2]) + stickers[0][i]
            dp[i][1] = max(dp[i-1][0], dp[i-1][2]) + stickers[1][i]
            dp[i][2] = max(dp[i-1][0], dp[i-1][1], dp[i-1][2])
        
        max_score = max(dp[n-1][0], dp[n-1][1], dp[n-1][2])
        results.append(max_score)
    
    return results

import sys
input = sys.stdin.read
data = input().split()

index = 0
T = int(data[index])
index += 1

test_cases = []
for _ in range(T):
    n = int(data[index])
    index += 1
    stickers = [
        list(map(int, data[index:index+n])),
        list(map(int, data[index+n:index+2*n]))
    ]
    index += 2*n
    test_cases.append(stickers)

results = max_sticker_score(test_cases)
for result in results:
    print(result)
