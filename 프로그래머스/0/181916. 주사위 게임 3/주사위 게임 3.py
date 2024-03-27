def solution(a, b, c, d):
    dice = [a, b, c, d]
    frequency = {x: dice.count(x) for x in set(dice)}

    if len(frequency) == 1:
        return 1111 * a
    elif 3 in frequency.values():
        p = [k for k, v in frequency.items() if v == 3][0]
        q = [k for k, v in frequency.items() if v == 1][0]
        return (10 * p + q) ** 2
    elif 2 in frequency.values() and len(frequency) == 2:
        p, q = frequency.keys()
        return (p + q) * abs(p - q)
    elif 2 in frequency.values() and len(frequency) == 3:
        p = [k for k, v in frequency.items() if v == 2][0]
        q, r = [k for k, v in frequency.items() if v == 1]
        return q * r
    else:
        return min(a, b, c, d)