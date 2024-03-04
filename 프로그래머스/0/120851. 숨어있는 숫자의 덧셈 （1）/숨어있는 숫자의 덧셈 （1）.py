def solution(my_string):
    answer = list(my_string)
    a = []
    b = []
    for i in answer:
        a.append(ord(i))
    for i in a:
        if i < 60:
            b.append(i-48)
    return sum(b)