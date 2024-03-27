def solution(intStrs, k, s, l):
    result = []
    for str_num in intStrs:
        sub_str_num = int(str_num[s:s+l])
        if sub_str_num > k:
            result.append(sub_str_num)
    return result