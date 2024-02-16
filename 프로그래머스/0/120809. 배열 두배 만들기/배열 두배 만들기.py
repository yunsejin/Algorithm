
def solution(numbers):
    from collections import deque
    q = deque(numbers)
    for i in numbers:
        q.popleft()
        q.append(i*2)
    return list(q)