def solve(n, m=0):
    if n < 0:
        return -1
    if n % 5 == 0:
        return m + n // 5
    return solve(n - 3, m + 1)

n = int(input())
print(solve(n))