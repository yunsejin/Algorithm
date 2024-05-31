from collections import deque

def is_valid(x, y, z, M, N, H):
    return 0 <= x < M and 0 <= y < N and 0 <= z < H

def solution(M, N, H, boxes):
    directions = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
    queue = deque()
    total_tomatoes = 0
    ripe_tomatoes = 0
    
    for z in range(H):
        for y in range(N):
            for x in range(M):
                if boxes[z][y][x] == 1:
                    queue.append((x, y, z, 0))
                    ripe_tomatoes += 1
                if boxes[z][y][x] != -1:
                    total_tomatoes += 1

    if ripe_tomatoes == total_tomatoes:
        return 0

    days = 0
    while queue:
        x, y, z, days = queue.popleft()
        for dx, dy, dz in directions:
            nx, ny, nz = x + dx, y + dy, z + dz
            if is_valid(nx, ny, nz, M, N, H) and boxes[nz][ny][nx] == 0:
                boxes[nz][ny][nx] = 1
                queue.append((nx, ny, nz, days + 1))
                ripe_tomatoes += 1

    if ripe_tomatoes == total_tomatoes:
        return days
    else:
        return -1

M, N, H = map(int, input().split())
boxes = []
for _ in range(H):
    box = []
    for _ in range(N):
        box.append(list(map(int, input().split())))
    boxes.append(box)

print(solution(M, N, H, boxes))
