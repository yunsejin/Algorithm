def solution(n, k):
    a = 12000
    b = 2000
    d = n
    c = 0
    if n < 10:
        answer = a*n + b*k
    else:
        while True:
            n -= 10
            c += 1
            if n < 10:
                break
        answer = a*d + b*k - c*b
    return answer