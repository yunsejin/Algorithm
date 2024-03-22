def solution(order):
    answer = 0
    a = list(str(order))
    print(a)
    for i in a:
        if i == '3' or i == '6' or i == '9':
            answer += 1
    return answer