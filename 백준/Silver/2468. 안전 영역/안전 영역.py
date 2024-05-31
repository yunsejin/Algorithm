from collections import deque

def bfs(matrix, visited, x, y, n, height):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque([(x, y)])
    visited[x][y] = True
    
    while queue:
        cx, cy = queue.popleft()
        
        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and matrix[nx][ny] > height:
                visited[nx][ny] = True
                queue.append((nx, ny))

def find_max_safe_areas(matrix, n):
    max_safe_areas = 0
    max_height = max(max(row) for row in matrix)
    
    for height in range(max_height + 1):
        visited = [[False] * n for _ in range(n)]
        safe_areas = 0
        
        for i in range(n):
            for j in range(n):
                if matrix[i][j] > height and not visited[i][j]:
                    bfs(matrix, visited, i, j, n, height)
                    safe_areas += 1
        
        max_safe_areas = max(max_safe_areas, safe_areas)
    
    return max_safe_areas

n = int(input().strip())
matrix = [list(map(int, input().split())) for _ in range(n)]

result = find_max_safe_areas(matrix, n)
print(result)
