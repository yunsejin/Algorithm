def solution(n):
    a = 0
    k = int(n**0.5//1)
    for i in range(1 ,  k+1 ):
        if n % i == 0:
            a+=1
    b = a*2
    if n**0.5%1 == 0:
        b -= 1
    return b