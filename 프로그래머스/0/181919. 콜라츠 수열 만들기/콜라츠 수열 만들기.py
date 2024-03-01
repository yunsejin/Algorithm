def solution(n):
    b = []
    while n != 1:
        b.append(n)
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
    b.append(1)
    return b