def solution(num_list):
    answer = []
    for i in range(5):
        answer.append(min(num_list))
        a = min(num_list)
        num_list.remove(a)
    answer.sort()
    return answer