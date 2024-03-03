def solution(n, k):
    answer = []
    a = k
    while True:
        if k > n:
            break
        answer.append(k)
        k = k + a
    return answer