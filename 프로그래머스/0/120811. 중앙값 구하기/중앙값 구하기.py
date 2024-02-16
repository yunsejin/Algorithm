def solution(array):
    from collections import deque
    array.sort()
    a = deque(array)
    b = len(array) // 2
    return a[b]