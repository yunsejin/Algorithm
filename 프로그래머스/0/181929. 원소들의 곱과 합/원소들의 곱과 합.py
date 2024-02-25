def solution(a):
    b = 1
    for i in a:
        b *= i
    if sum(a)**2 >= b:
        return 1
    else:
        return 0