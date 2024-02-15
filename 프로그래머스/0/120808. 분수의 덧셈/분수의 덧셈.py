def solution(numer1, denom1, numer2, denom2):
    c = denom1 * denom2
    d = numer1 * denom2 + numer2 * denom1
    a = denom1 * denom2
    b = numer1 * denom2 + numer2 * denom1
    while b:
        if a > b:
            a, b = b, a
        b %= a
    c = c // a
    d = d // a
    e=[]
    e.append(d)
    e.append(c)
    return e