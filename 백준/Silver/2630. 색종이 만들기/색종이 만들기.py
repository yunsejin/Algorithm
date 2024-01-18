N = int(input())
bitlist = [list(map(int, input().split())) for _ in range(N)]
result = [0, 0]

def divide(x, y, N):
    global result
    color = bitlist[x][y]

    for i in range(x, x + N):
        for j in range(y, y + N):
            if color != bitlist[i][j]:
                divide(x, y, N // 2)
                divide(x + N // 2, y, N // 2)
                divide(x, y + N // 2, N // 2)
                divide(x + N // 2, y + N // 2, N // 2)
                return

    if color == 0:
        result[0] += 1
    else:
        result[1] += 1

divide(0, 0, N)
print(result[0])
print(result[1])
