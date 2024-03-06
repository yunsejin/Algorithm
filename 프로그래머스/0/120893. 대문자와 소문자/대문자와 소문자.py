def solution(my_string):
    a = list(my_string)
    answer = []
    for i in a:
        if i.isupper():
            answer.append(i.lower())
        else:
            answer.append(i.upper())
    return ''.join(answer)