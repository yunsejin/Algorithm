def solution(my_string):
    a = {}
    for i in my_string:
        if i not in a:
            a[i] = 1
        else:
            a[i] += 1
    answer = []
    for i in a:
        answer.append(i)
    return ''.join(answer)