def solution(my_string, letter):
    my_string.strip()
    answer = []
    for i in my_string:
        if i != letter:
            answer.append(i)
    return ''.join(answer)