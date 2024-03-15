def solution(n_str):
    n_str = list(n_str)
    while n_str[0] == '0':
        n_str.pop(0)
    return ''.join(n_str)