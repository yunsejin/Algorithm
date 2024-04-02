def solution(my_string):
    dp = [0] * 52
    for i in range(len(my_string)):
        if ord(my_string[i]) >= 97:
            dp[ord(my_string[i]) - 71] += 1
        else:
            dp[ord(my_string[i]) - 65] += 1
    return dp