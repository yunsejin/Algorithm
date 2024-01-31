N, K = map(int,input().split(' '))
use = list(map(int,input().split(' ')))
code = []
answer = 0

for i in range(K):
    if use[i] in code : 
        continue

    if len(code) < N :
        code.append(use[i])
        continue

    priority = []
    for j in code:
        if j in use[i:]:
            priority.append(use[i:].index(j))
        else:
            priority.append(101)
    target = priority.index(max(priority))
    code.remove(code[target])
    code.append(use[i])
    answer += 1

print(answer)