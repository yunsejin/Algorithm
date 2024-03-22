def solution(my_string):
    answer = []
    for i in my_string:
        if i.isdigit():
            answer.append(i)
    answer.sort()
    for i in range(len(answer)):
        answer[i] = int(answer[i])
    return answer