def solution(start_num, end_num):
    f = end_num - start_num
    answer = []
    for i in range(f+1):
        answer.append(start_num+i)
    return answer