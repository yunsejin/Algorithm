def solution(myString):
    a = []
    list(myString)
    b = []
    for i in myString:
        a.append(ord(i))
    for i in a:
        if i < 108:
            b.append('l')
        else:
            b.append(chr(i))
    return ''.join(b)