def solution(my_string):
    list = []
    for i in range(len(my_string)):
        list.append(my_string[-i:])
    list.sort()
    return list