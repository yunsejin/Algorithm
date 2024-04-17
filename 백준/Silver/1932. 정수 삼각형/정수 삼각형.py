n = int(input())
LLLList = []
for i in range(n):
    LLLList.append(list(map(int, input().split())))
dp = [[0]*n for _ in range(n)]
if n == 1:
    print(LLLList[0][0])
    exit()
dp[0][0] = LLLList[0][0]
for i in range(1, n):
    for j in range(i+1):
        dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + LLLList[i][j]
print(max(dp[n-1]))