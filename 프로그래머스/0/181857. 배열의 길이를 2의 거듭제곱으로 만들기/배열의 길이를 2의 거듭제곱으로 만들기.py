def solution(arr):
    answer = arr
    dp = [0] * 1001
    for i in range(len(arr)):
        dp[i] = 2**i
    if not len(arr) in dp:
        while not len(answer) in dp:
            answer.append(0)
    return answer