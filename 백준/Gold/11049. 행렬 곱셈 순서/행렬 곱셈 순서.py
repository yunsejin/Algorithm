import sys
input = sys.stdin.readline

def matrix_chain_order(p):
    n = len(p) - 1
    dp = [[0] * len(p) for _ in range(len(p))]

    for length in range(2, n + 1):
        for i in range(1, n - length + 2):
            j = i + length - 1
            dp[i][j] = sys.maxsize
            for k in range(i, j):
                cost = dp[i][k] + dp[k+1][j] + p[i-1] * p[k] * p[j]
                if cost < dp[i][j]:
                    dp[i][j] = cost

    return dp[1][n]

N = int(input())
hang = [list(map(int, input().split())) for _ in range(N)]

p = [hang[0][0]] + [sizes[1] for sizes in hang]

print(matrix_chain_order(p))