def solution(my_string, n):
    my_string.strip()
    answer = []
    for i in my_string:
        answer.append(i*n)
    return ''.join(answer)