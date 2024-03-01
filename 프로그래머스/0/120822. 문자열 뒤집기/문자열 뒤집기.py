def solution(my_string):
    b = []
    my_string.strip()
    for i in range(len(my_string)):
        b.append(my_string[i])
    b.reverse()
    return ''.join(b)