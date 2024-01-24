from collections import deque
n,m=map(int,input().split())
g=[list(map(int,input().rstrip())) for _ in range(n)]
dis=[(-1,0),(1,0),(0,-1),(0,1)]
def bfs(x,y):
    q=deque([(x,y)])
    while q:
        x,y=q.popleft()
        for dx,dy in dis:
            nx,ny=x+dx,y+dy
            if 0<=nx<n and 0<=ny<m and g[nx][ny]==1:
                g[nx][ny]=g[x][y]+1
                q.append((nx,ny))
    return g[-1][-1]
print(bfs(0,0))