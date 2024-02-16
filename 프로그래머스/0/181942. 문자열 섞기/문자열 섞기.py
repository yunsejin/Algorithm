def solution(str1, str2):
    min_len = min(len(str1), len(str2))
    a = []
    for i in range(min_len):
        a.append(str1[i])
        a.append(str2[i])
    return ''.join(a)