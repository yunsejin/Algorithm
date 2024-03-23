def solution(my_string, m, c):
    a = []
    for i in range(c-1, len(my_string), m):
        a.append(my_string[i])
    return ''.join(a)
