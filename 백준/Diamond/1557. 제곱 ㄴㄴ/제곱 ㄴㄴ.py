from math import isqrt

def count_square_free(n):
    mobius = [1] * (isqrt(n) + 1)
    for i in range(2, len(mobius)):
        if mobius[i] == 1:
            for j in range(i, len(mobius), i):
                mobius[j] *= -i
            if i * i < len(mobius):
                for j in range(i * i, len(mobius), i * i):
                    mobius[j] = 0
    for i in range(2, len(mobius)):
        if mobius[i] == i:
            mobius[i] = 1
        elif mobius[i] == -i:
            mobius[i] = -1
        elif mobius[i] < 0:
            mobius[i] = 1
        elif mobius[i] > 0:
            mobius[i] = -1

    count = 0
    for i in range(1, len(mobius)):
        if mobius[i]:
            count += mobius[i] * (n // (i * i))
    return count

def find_kth_square_free(k):
    left, right = 1, 2*k
    while left < right:
        mid = (left + right) // 2
        if count_square_free(mid) < k:
            left = mid + 1
        else:
            right = mid
    return left


k = int(input())
print(find_kth_square_free(k))