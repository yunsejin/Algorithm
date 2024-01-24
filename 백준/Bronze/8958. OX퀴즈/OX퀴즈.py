import sys

n = int(sys.stdin.readline())

for i in range(n):
    a = sys.stdin.readline()
    score = 0
    cnt = 0
    for j in a:
        if j == "O":
            cnt += 1
            score += cnt
        else:
            cnt = 0
    print(score)