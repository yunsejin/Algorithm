from collections import deque

def bfs(n, m, grid, start):
    # 이동할 네 방향 정의 (상, 하, 좌, 우)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque([start])
    distances = [[-1] * m for _ in range(n)]
    sx, sy = start
    distances[sx][sy] = 0

    while queue:
        x, y = queue.popleft()

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 1 and distances[nx][ny] == -1:
                distances[nx][ny] = distances[x][y] + 1
                queue.append((nx, ny))
    
    return distances

n, m = map(int, input().split())
grid = []
start = None

for i in range(n):
    row = list(map(int, input().split()))
    for j in range(m):
        if row[j] == 2:
            start = (i, j)
    grid.append(row)

distances = bfs(n, m, grid, start)

for i in range(n):
    for j in range(m):
        if grid[i][j] == 0:
            print(0, end=' ')
        else:
            print(distances[i][j], end=' ')
    print()
