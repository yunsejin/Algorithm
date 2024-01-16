import sys
from collections import deque
N = int(sys.stdin.readline())

queue=deque([])

for i in range(N):
    A = sys.stdin.readline().split()
    if A[0] == 'push':
        queue.append(A[1])
    if A[0] == 'pop':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.popleft())
    if A[0] == 'size':
        print(len(queue))
    if A[0] == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    if A[0] == 'front':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    if A[0] == 'back':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])
