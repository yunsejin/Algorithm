from collections import deque

n = int(input())

def solve(n):
  queue = deque(range(1, n + 1))
  while len(queue) > 1:
    queue.popleft()
    queue.append(queue.popleft())
  return queue.popleft()

print(solve(n))