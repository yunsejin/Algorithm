inning_w_ulrim = list(map(int, input().split()))
inning_w_startlink = list(map(int, input().split()))


score_ulrim = 0
score_startlink = 0


for i in range(9):
    score_ulrim += inning_w_ulrim[i]
    if score_ulrim > score_startlink:
        print('Yes')
        break
    score_startlink += inning_w_startlink[i]
else:
    print('No')
