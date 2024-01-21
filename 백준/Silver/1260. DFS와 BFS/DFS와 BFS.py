N,M,V = map(int,input().split())

graph = [[] for _ in range(N+1)]
for i in range (M):
    a,b = map(int,input().split())
    graph[a]+= [b]
    graph[b]+= [a]

for i in range(N+1):
    graph[i].sort()

visited1 = [0]*(N+1)
visited2 = visited1.copy()

def dfs(V):
    visited1[V] = 1
    print(V, end=' ')
    for i in graph[V]:
        if visited1[i] == 0:
            dfs(i)

def bfs(V):
    queue = [V]
    visited2[V] = 1
    while queue:
        V = queue.pop(0)
        print(V, end = ' ')
        for i in graph[V]:
            if(visited2[i] == 0):
                queue.append(i)
                visited2[i] = 1

dfs(V)
print()
bfs(V)