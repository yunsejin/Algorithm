def solution(myString):
    myString.strip()
    b = []
    for i in myString:
        b.append(i.upper())
    return ''.join(b)