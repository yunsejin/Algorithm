def solution(hp):
    answer = 0
    while hp != 0:
        answer += 1
        hp -= 5
        if hp < 0:
            hp += 5
            hp -= 3
        if hp < 0:
            hp += 3
            hp -= 1
    return answer