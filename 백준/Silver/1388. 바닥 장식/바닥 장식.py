import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

n, m = map(int, input().split())
g = [list(input()) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
cnt = 0

def dfs(x, y):
    stack = [(x, y)]
    while stack:
        x, y = stack.pop()
        if visited[x][y]:
            continue
        visited[x][y] = 1
        if g[x][y] == '-':
            ny = y + 1
            while ny < m and g[x][ny] == '-' and not visited[x][ny]:
                stack.append((x, ny))
                ny += 1
        else:
            nx = x + 1
            while nx < n and g[nx][y] == '|' and not visited[nx][y]:
                stack.append((nx, y))
                nx += 1

for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            dfs(i, j)
            cnt += 1

print(cnt)