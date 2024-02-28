from sys import stdin
from collections import deque
N = int(stdin.readline())
Que = deque()

for i in range(N):
    A = stdin.readline().split()

    if A[0] == 'push_front':
        Que.appendleft(A[1])
    elif A[0] == 'push_back':
        Que.append(A[1])
    elif A[0] == 'pop_front':
        if Que:
            print(Que.popleft())
        else:
            print(-1)
    elif A[0] == 'pop_back':
        if Que:
            print(Que.pop())
        else:
            print(-1)
    elif A[0] == 'size':
        print(len(Que))
    elif A[0] == 'empty':
        print(1 if not Que else 0)
    elif A[0] == 'front':
        print(Que[0] if Que else -1)
    elif A[0] == 'back':
        print(Que[-1] if Que else -1)