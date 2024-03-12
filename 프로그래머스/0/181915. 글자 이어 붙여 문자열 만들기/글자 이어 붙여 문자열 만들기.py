def solution(my_string, index_list):
    a = list(my_string)
    b = []
    for i in index_list:
        b.append(a[i])
    return ''.join(b)