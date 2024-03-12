def solution(str1, str2):
    answer = ''
    if str1 in str2:
        answer += str1
        return 1
    else:
        return 0