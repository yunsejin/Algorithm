n = int(input())
LLLList = []
for i in range(n):
    LLLList.append(list(map(int, input().split())))
dp = [[0]*n for _ in range(n)]
if n == 1:
    print(LLLList[0][0])
    exit()
dp[0][0] = LLLList[0][0]
dp[1][0] = LLLList[0][0] + LLLList[1][0]
dp[1][1] = LLLList[0][0] + LLLList[1][1]
for i in range(2, n):
    for j in range(i+1):
        if j == 0:
            dp[i][j] = dp[i-1][j] + LLLList[i][j]
        elif j == i:
            dp[i][j] = dp[i-1][j-1] + LLLList[i][j]
        else:
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + LLLList[i][j]
print(max(dp[n-1]))