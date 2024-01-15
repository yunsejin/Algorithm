T = int(input())
results = []

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

for _ in range(T):
    n = int(input())
    for i in range(n//2, n):
        if is_prime(i) and is_prime(n - i):
            results.append((i, n - i))
            break

for result in results:
    print(result[1], result[0])
