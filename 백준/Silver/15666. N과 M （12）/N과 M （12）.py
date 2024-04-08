from itertools import combinations_with_replacement

N, M = map(int, input().split())
numbers = sorted(list(map(int, input().split())))

result_set = set(combinations_with_replacement(numbers, M))

for seq in sorted(result_set):
    print(' '.join(map(str, seq)))