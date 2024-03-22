def solution(num, k):
    answer = list(str(num))
    for i in range(len(answer)):
        print(answer[i])
        if answer[i] == str(k):
            return i+1
    return -1