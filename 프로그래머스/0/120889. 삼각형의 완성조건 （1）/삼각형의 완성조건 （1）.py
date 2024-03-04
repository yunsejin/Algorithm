def solution(sides):
    if sides[0] == sides[1] == sides[2]:
        return 1
    else:
        a = max(sides)
        b = 0
        for i in sides:
            if i == a:
                sides.remove(i)
        if a >= sum(sides):
            return 2
        else:
            return 1