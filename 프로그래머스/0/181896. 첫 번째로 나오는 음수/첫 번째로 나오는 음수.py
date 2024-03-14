def solution(num_list):
    answer = []
    for i in range(len(num_list)):
        if num_list[i] < 0:
            answer.append(i)
    if answer == []:
        return -1
    else:
        return answer[0]