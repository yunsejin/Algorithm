def solution(my_string, is_suffix):
    a = list(my_string)
    b = list(is_suffix)
    c = []
    if len(my_string) < len(is_suffix):
        return 0
    for i in range(1,1+len(is_suffix)):
        if a[-i] == b[-i]:
            c.append(b[-i])
    c.reverse()
    if c == b:
        return 1
    else:
        return 0