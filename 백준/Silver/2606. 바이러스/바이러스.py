n=int(input())
v=int(input())
graph = [[] for i in range(n+1)]
visited=[0]*(n+1)
for i in range(v):
    a,b=map(int,input().split())
    graph[a]+=[b]
    graph[b]+=[a]
def bfs(v):
    queue=[v]
    visited[v]=1
    while queue:
        v=queue.pop(0)
        for nx in graph[v]:
            if visited[nx]==0:
                visited[nx]=1
                queue.append(nx)
bfs(1)
print(sum(visited)-1)