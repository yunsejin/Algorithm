def solution(my_string):
    a = ['a','e','i','o','u']
    b = list(my_string)
    c = b.copy()
    for i in b:
        if i in a:
            c.remove(i)
    return ''.join(c)