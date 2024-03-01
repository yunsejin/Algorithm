def solution(money):
    answer = []
    a = 0
    while money >= 5500:
        a += 1
        money -= 5500
    answer.append(a)
    answer.append(money)
    return answer