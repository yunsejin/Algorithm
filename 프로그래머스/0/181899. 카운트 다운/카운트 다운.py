def solution(start, end_num):
    answer = []
    for i in range(start-end_num+1):
        answer.append(end_num+i)
    answer.reverse()
    return answer