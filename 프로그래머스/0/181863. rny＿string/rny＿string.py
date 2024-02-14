def solution(rny_string):
    lmlml = ""
    for i in rny_string:
        if i == 'm':
            lmlml += 'rn'
        else:
            lmlml += i
    return lmlml