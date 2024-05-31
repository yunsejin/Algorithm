from collections import deque

def bfs(x, y, visited, field, n, m):
    color = field[x][y]
    queue = deque([(x, y)])
    visited[x][y] = True
    count = 0
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] # 상, 하, 좌, 우
    
    while queue:
        cx, cy = queue.popleft()
        count += 1
        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny] and field[nx][ny] == color:
                visited[nx][ny] = True
                queue.append((nx, ny))
                
    return count

def calculate_power(n, m, field):
    visited = [[False] * n for _ in range(m)]
    your_power = 0
    enemy_power = 0
    
    for i in range(m):
        for j in range(n):
            if not visited[i][j]:
                soldiers_count = bfs(i, j, visited, field, n, m)
                if field[i][j] == 'W':
                    your_power += soldiers_count ** 2
                else:
                    enemy_power += soldiers_count ** 2
    
    return your_power, enemy_power

n, m = map(int, input().split())
field = [input().strip() for _ in range(m)]

your_power, enemy_power = calculate_power(n, m, field)

print(your_power, enemy_power)
