n, v = map(int, input().split())
graph = [[] for i in range(n+1)]
visited=[0]*(n+1)
for i in range(v):
    a,b=map(int,input().split())
    graph[a]+=[b]
    graph[b]+=[a]
def dfs(v):
    visited[v]=1
    for i in graph[v]:
        if visited[i]==0:
            dfs(i)
cnt=0
for i in range(1,n+1):
    if visited[i]==0:
        dfs(i)
        cnt+=1
print(cnt)