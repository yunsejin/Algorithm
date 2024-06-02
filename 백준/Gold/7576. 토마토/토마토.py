from collections import deque

def solution():
    M, N = map(int, input().split())
    box = []
    for _ in range(N):
        box.append(list(map(int, input().split())))
    
    queue = deque()
    for i in range(N):
        for j in range(M):
            if box[i][j] == 1:
                queue.append((i, j))

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    while queue:
        x, y = queue.popleft()
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and box[nx][ny] == 0:
                box[nx][ny] = box[x][y] + 1
                queue.append((nx, ny))
    
    max_days = 0
    for row in box:
        for value in row:
            if value == 0:
                print(-1)
                return
            max_days = max(max_days, value)
    
    print(max_days - 1 if max_days != 1 else 0)

solution()
