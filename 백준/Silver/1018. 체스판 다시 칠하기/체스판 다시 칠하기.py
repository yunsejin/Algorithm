N, M = map(int, input().split())
S = list(input() for _ in range(N))

def count(x, y, color):
    changes = 0
    for i in range(x, x + 8):
        for j in range(y, y + 8):
            if (i + j) % 2 == 0:
                if S[i][j] != color:
                    changes += 1
            else:
                if S[i][j] == color:
                    changes += 1
    return changes

min_changes = float('inf')
for i in range(N - 7):
    for j in range(M - 7):
        W = count(i, j, 'W')
        B = count(i, j, 'B')
        min_changes = min(min_changes, W, B)

print(min_changes)