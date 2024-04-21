from itertools import combinations
from math import gcd

def lcm(x, y):
    return x * y // gcd(x, y)

def find_least_majority_multiple(numbers):
    min_lcm = float('inf')
    for combo in combinations(numbers, 3):
        current_lcm = lcm(lcm(combo[0], combo[1]), combo[2])
        if current_lcm < min_lcm:
            min_lcm = current_lcm
    return min_lcm

input_numbers = map(int, input().split())
print(find_least_majority_multiple(input_numbers))