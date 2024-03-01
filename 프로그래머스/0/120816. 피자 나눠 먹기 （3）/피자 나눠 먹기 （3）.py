def solution(slice, n):
    answer = 1
    if slice * answer >= n:
        return answer
    else:
        while True:
            if (slice * answer) >= n:
                return answer
            else:
                answer += 1
        