N, M = map(int, input().split())
ans = []

def dfs(lst):
    if len(lst) == M: 
        print(*lst)
        return
    
    for i in range(1, N+1):
        dfs(lst + [i])

dfs([])
