while True:
    a = int(input())
    if a == 0:
        break
    c = 0
    for i in range(a):
        c += a-i
    print(c)