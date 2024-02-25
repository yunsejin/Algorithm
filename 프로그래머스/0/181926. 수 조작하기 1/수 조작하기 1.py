def solution(n, control):
    a = list(map(str,control.strip()))
    for i in a:
        if i == "w":
            n += 1
        elif i == "s":
            n -= 1
        elif i == "d":
            n += 10
        else:
            n -= 10
    return n
    