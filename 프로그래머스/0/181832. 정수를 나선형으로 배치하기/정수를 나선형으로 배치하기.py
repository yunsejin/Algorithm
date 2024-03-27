def solution(n):
    matrix = [[0] * n for _ in range(n)]
    
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    
    x, y = 0, 0
    num = 1
    direction = 0
    
    for i in range(n ** 2):
        matrix[x][y] = num
        num += 1
        nx, ny = x + dx[direction], y + dy[direction]
        if nx < 0 or nx >= n or ny < 0 or ny >= n or matrix[nx][ny] != 0:
            direction = (direction + 1) % 4
            nx, ny = x + dx[direction], y + dy[direction]
        x, y = nx, ny
    
    return matrix