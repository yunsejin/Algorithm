a, b = map(int, input().split())

s = []

def dfs(x):
    if len(s) == b:
        print(' '.join(map(str, s)))
        return
    for i in range(x, a+1):
        s.append(i)
        dfs(i)
        s.pop()
dfs(1)