n = int(input())

def factorial(n):
    count = 0
    while n >= 5:
        n //= 5
        count += n
    return count

print(factorial(n))