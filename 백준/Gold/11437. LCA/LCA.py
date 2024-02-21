import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e5))
LOG = 21

n = int(input())
node = [[] for _ in range(n+1)]
parent = [[0] * LOG for _ in range(n+1)]
depth = [0] * (n+1)
visited = [False] * (n+1)

for _ in range(n-1):
    a, b = map(int, input().split())
    node[a].append(b)
    node[b].append(a)

def dfs(x, d):
    visited[x] = True
    depth[x] = d
    for y in node[x]:
        if visited[y]:
            continue
        parent[y][0] = x
        dfs(y, d+1)

def set_parent():
    dfs(1, 0)
    for i in range(1, LOG):
        for j in range(1, n+1):
            parent[j][i] = parent[parent[j][i-1]][i-1]

def lca(a, b):
    if depth[a] > depth[b]:
        a, b = b, a
    for i in range(LOG-1, -1, -1):
        if depth[b] - depth[a] >= (1 << i):
            b = parent[b][i]
    if a == b:
        return a
    for i in range(LOG-1, -1, -1):
        if parent[a][i] != parent[b][i]:
            a = parent[a][i]
            b = parent[b][i]
    return parent[a][0]

set_parent()

m = int(input())
for _ in range(m):
    a, b = map(int, input().split())
    print(lca(a, b))
