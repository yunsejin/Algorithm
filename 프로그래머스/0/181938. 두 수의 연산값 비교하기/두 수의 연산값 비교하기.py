def solution(a, b):
    c = int(str(a) + str(b))
    d = 2 * a * b
    if c >= d:
        return c
    else:
        return d