def solution(num_list):
    first = []
    second = []

    for a in num_list:
        if a%2 :
            first.append(a)
        else : second.append(a)

    ans1 = 0
    ans2 = 0
    for i in first:
        ans1 *= 10
        ans1 += i

    for i in second:
        ans2 *= 10
        ans2 += i
    return ans1+ans2