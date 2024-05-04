while True:
    try:
        a = input()
        b = []
        for i in a:
            if i == 'i':
                b.append('e')
            elif i == 'e':
                b.append('i')
            elif i == 'I':
                b.append('E')
            elif i == 'E':
                b.append('I')
            else:
                b.append(i)
        print(''.join(b))
    except:
        break