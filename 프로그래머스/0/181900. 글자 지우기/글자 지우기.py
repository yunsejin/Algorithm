def solution(my_string, indices):
    my_string_list = list(my_string)
    for index in indices:
        my_string_list[index] = None
    return ''.join([char for char in my_string_list if char is not None])