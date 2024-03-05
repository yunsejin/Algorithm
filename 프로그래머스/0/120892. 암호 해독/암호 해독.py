def solution(cipher, code):
    from collections import deque
    answer = deque()
    a = list(cipher)
    if code == 1:
        return cipher
    elif code == 0:
        return ''
    else:
        for i in range(1 , len(a)):
            if (i+1) % code == 0:
                answer.append(a[i])
        return ''.join(answer)