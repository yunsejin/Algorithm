def is_composite(num):
    if num < 4:
        return False
    divisor_count = 0
    for i in range(1, num + 1):
        if num % i == 0:
            divisor_count += 1
        if divisor_count > 2:
            return True
    return False

def solution(n):
    composite_count = 0
    for num in range(1, n + 1):
        if is_composite(num):
            composite_count += 1
    return composite_count