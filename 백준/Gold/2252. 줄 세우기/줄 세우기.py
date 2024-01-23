from collections import deque
n,m=map(int,input().split())
g=[[] for _ in range(n+1)]
indegree=[0]*(n+1)

for i in range(m):
    a,b=map(int,input().split())
    g[a].append(b)
    indegree[b]+=1

q=deque()
for i in range(1,n+1):
    if indegree[i]==0:
        q.append(i)
while q:
    now=q.popleft()
    print(now,end=" ")
    for next in g[now]:
        indegree[next]-=1
        if indegree[next]==0:
            q.append(next)