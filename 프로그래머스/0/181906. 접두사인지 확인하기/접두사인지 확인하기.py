def solution(my_string, is_prefix):
    a = list(my_string)
    b = list(is_prefix)
    if len(a) < len(b):
        return 0
    for i in range(len(b)):
        if a[i] != b[i]:
            return 0
    return 1