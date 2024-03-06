def solution(array):
    a = []
    for i in range(len(array)):
        a.append([array[i],i])
    a.sort()
    return a[-1]