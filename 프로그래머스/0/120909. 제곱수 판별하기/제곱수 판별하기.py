def solution(n):
    a = n
    b = int(n**0.5)
    if int(b**2) == int(a):
        return 1
    else:
        return 2