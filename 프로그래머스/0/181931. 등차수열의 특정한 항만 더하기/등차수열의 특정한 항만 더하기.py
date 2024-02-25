def solution(a, d, included):
    sum = 0
    for i in range(len(included)):
        if included[i] == True:
            sum += a
        print(sum)
        a += d
    return sum