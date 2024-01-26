N,M = map(int,input().split())
box = [[0,0]]
for _ in range(N):
    box.append(list(map(int,input().split())))
list = [[0]*(M+1) for _ in range(N+1)]
for i in range(1,N+1):
    for j in range(1,M+1):
        if box[i][0] > j:
            list[i][j] = list[i-1][j]
        else:
            list[i][j] = max(list[i-1][j],list[i-1][j-box[i][0]]+box[i][1])
print(list[N][M])