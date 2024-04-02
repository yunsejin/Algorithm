def solution(myStr):
    answer = []
    for i in myStr:
        if i == 'a' or i == 'b' or i == 'c':
            answer.append(" ")
        else:
            answer.append(i)
    answer = ''.join(answer)
    b = []
    for i in answer.split():
        b.append(i)
    return b