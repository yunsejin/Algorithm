def solution(n, slicer, num_list):
    answer = []
    if n == 1:
        for i in range(slicer[1]+1):
            answer.append(num_list[i])
    if n == 2:
        for i in range(slicer[0], len(num_list)):
            answer.append(num_list[i])
    if n == 3:
        for i in range(slicer[0], slicer[1]+1):
            answer.append(num_list[i])
    if n == 4:
        for i in range(slicer[0], slicer[1]+1, slicer[2]):
            answer.append(num_list[i])
    return answer