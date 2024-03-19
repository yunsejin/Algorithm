def solution(number):
    list(number)
    a = 0
    for i in number:
        a += int(i)
    return a%9