def solution(emergency):
    a = []
    for i in range(len(emergency)):
        a.append([emergency[i] , i+1 , 0])
    a.sort(reverse = True)
    for i in range(len(a)):
        a[i][2] = i+1
    a.sort(key = lambda  x:(x[1]))
    ans = []
    for i in a:
        ans.append(i[2])
    return ans