def solution(l, r):
    arr = []
    for i in range(l,r+1):
        a = i
        while True:
            if i == 5 or i == 0:
                arr.append(a)
                break
            if i % 10 == 0 or i % 10 == 5:
                i = i // 10
            else:
                break
    if len(arr) == 0:
        return [-1]
    else:
        return arr