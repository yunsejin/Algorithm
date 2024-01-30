import sys
input = sys.stdin.readline

X, Y = map(int, input().split())
N = int(input())

sudle = [[0, X], [0, Y]]

for _ in range(N):
    su_a, su_b = map(int, input().split())
    if su_a == 0:
        sudle[1].append(su_b)
    else:
        sudle[0].append(su_b)

sudle[0].sort()
sudle[1].sort()

carzil_1 = max(sudle[0][i+1] - sudle[0][i] for i in range(len(sudle[0])-1))
carzil_2 = max(sudle[1][i+1] - sudle[1][i] for i in range(len(sudle[1])-1))

print(carzil_1 * carzil_2)