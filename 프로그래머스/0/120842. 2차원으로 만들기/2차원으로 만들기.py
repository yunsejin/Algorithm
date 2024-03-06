def solution(num_list, n):
    answer = []
    if len(num_list) % n == 0:
        for i in range(0, len(num_list), n):
            answer.append(num_list[i:i + n])
    else:
        for i in range(0, len(num_list)-1, n):
            answer.append([num_list[i:i + n]])
        answer.append(num_list[-1])
    return answer