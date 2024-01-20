n=int(input())
v=int(input())
graph = [[] for i in range(n+1)]
visited=[0]*(n+1)

for i in range(v):
    a,b=map(int,input().split())
    graph[a]+=[b]
    graph[b]+=[a]
    
def dfs(v):
    stack=[v]
    while stack:
        v=stack.pop()
        if visited[v]==0:
            visited[v]=1
            stack+=graph[v]

dfs(1)
print(sum(visited)-1)