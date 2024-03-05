n,m = list(map(int,input().split()))
a = []
def dfs(start):
    if len(a)==m:
        print(' '.join(map(str,a)))
        return
    
    for i in range(start,n+1):
        if i not in a:
            a.append(i)
            dfs(i+1)
            a.pop()
dfs(1)