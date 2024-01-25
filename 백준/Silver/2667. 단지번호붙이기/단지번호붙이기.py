import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline
from collections import deque

n = int(input())
g = [list(map(int, input().rstrip())) for _ in range(n)]
size = []

def init(n, g):
    m = len(g[0])
    dis = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    def bfs(x, y):
        q = deque([(x, y)])
        count = 0
        while q:
            x, y = q.popleft()
            if g[x][y] == 1:
                count += 1
                g[x][y] = 0
                for dx, dy in dis:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < m:
                        q.append((nx, ny))
        return count

    count = 0
    for i in range(n):
        for j in range(m):
            if g[i][j] == 1:
                count += 1
                size.append(bfs(i, j))
    size.sort()
    return count, size

result = init(n, g)
print(result[0])
for size in result[1]:
    print(size)