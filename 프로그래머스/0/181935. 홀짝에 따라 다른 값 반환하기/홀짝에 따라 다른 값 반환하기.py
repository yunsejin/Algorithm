def solution(n):
    a = n
    b = n
    for i in range(n+1):
        if(i % 2 == 1):
            b += i
        else:
            a += i**2
        print(a,b)
    return a-n if n % 2 == 0 else b-n