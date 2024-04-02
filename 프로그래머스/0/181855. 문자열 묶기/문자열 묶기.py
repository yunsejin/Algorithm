def solution(strArr):
    a = []
    for i in strArr:
        a.append(len(i))
    a.sort()
    b = []
    c = 1
    for i in range(1,len(a)):
        if a[i] == a[i-1]:
            c += 1
        if a[i] != a[i-1]:
            b.append(c)
            c = 1
        b.append(c)
    return max(b)