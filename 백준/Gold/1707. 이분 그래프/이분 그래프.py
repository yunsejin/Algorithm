import sys
input = sys.stdin.readline

K = int(input())

def dfs(V, state):
    stack = [(V, state)]
    while stack:
        V, state = stack.pop()
        visited[V] = state
        for i in graph[V]:
            if visited[i] == 0:
                stack.append((i, -state))
            elif visited[i] == visited[V]:
                return False
    return True

for _ in range(K):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    for _ in range(E):
        a, b = map(int, input().split())
        graph[a] += [b]
        graph[b] += [a]
    visited = [0] * (V+1)

    res = True

    for k in range(1, V+1):
        if visited[k] == 0:
            res = dfs(k, 1)
            if not res:
                break

    print('YES' if res else 'NO')
