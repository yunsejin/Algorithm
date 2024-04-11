from collections import deque

def bfs(start, graph):
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    queue = deque([start])
    visited = set([start])
    count = 0
    
    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(graph) and 0 <= ny < len(graph[0]) and (nx, ny) not in visited:
                if graph[nx][ny] != 'X':
                    visited.add((nx, ny))
                    queue.append((nx, ny))
                    if graph[nx][ny] == 'P':
                        count += 1
    return count

N, M = map(int, input().split())
campus = [list(input().strip()) for _ in range(N)]

for i in range(N):
    for j in range(M):
        if campus[i][j] == 'I':
            start = (i, j)

result = bfs(start, campus)
if result > 0:
    print(result)
else:
    print("TT")