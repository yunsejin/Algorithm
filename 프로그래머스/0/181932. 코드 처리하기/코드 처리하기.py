def solution(code):
    mode = 0
    a = []
    for i in range(len(code)):
        if mode == 0:
            if code[i] != '1':
                if i % 2 == 0:
                    a.append(code[i])
            else:
                mode = 1
        else:
            if code[i] != '1':
                if i % 2 == 1:
                    a.append(code[i])
            else:
                mode = 0
    if not a:
        return 'EMPTY'
    return ''.join(a)