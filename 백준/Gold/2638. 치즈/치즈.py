from collections import deque

N,M=map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]

def bfs(arr):
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    count = 0
    lista = deque()
    air = 0
    lista.append([0,0])
    while True:
        while lista:
            i,j = lista.popleft()
            if arr[i][j] != 2:
                air +=1
                arr[i][j] = 2
                for _ in range(4):
                    x = dx[_] + i
                    y = dy[_] + j
                    if -1 < x < N and -1 < y < M and arr[x][y] == 0 :
                        lista.append([x,y])

        for i in range(N):
            for j in range(M):
                number = 4
                if arr[i][j] == 1:
                     for _ in range(4):
                        x = dx[_] + i
                        y = dy[_] + j
                        if arr[x][y] ==2:
                            number -= 1
                if number <=2:
                    arr[i][j] = "C"

        for i in range(N):
            for j in range(M):
                if arr[i][j] == "C":
                    arr[i][j] = 0
                    lista.append([i,j])     

     
        count += 1 
        if air == N*M:
            print(count-1)
            break

                
bfs(arr)                