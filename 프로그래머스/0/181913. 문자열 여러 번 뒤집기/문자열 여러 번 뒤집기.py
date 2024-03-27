def solution(my_string, queries):
    a = list(my_string)
    for i in queries:
        a[i[0]:i[1]+1] = a[i[0]:i[1]+1][::-1]
    return ''.join(a)