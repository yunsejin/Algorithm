def modular_exponentiation(a, b, c):
    if b == 0:
        return 1
    half = modular_exponentiation(a, b // 2, c)
    half = (half * half) % c
    if b % 2 == 0:
        return half
    else:
        return (half * a) % c

a, b, c = map(int, input().split())

result = modular_exponentiation(a, b, c)
print(result)
