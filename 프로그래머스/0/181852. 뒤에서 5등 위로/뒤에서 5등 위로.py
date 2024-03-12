def solution(num_list):
    num_list.sort()
    for i in range(0, 5):
        num_list.pop(0)
    return num_list