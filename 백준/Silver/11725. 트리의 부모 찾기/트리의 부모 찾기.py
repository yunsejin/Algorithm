import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline
n = int(input())
graph = [[] for i in range(n + 1)]
visited = [0] * (n + 1)
for i in range(n - 1):
    a, b = map(int, input().strip().split())
    graph[a] += [b]
    graph[b] += [a]

parent = [0] * (n + 1)

def dfs(v):
    visited[v] = 1
    for nx in graph[v]:
        if visited[nx] == 0:
            parent[nx] = v
            dfs(nx)

dfs(1)
for i in range(2, n + 1):
    print(parent[i])