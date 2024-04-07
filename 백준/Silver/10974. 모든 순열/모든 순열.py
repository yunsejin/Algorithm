from itertools import permutations

n = int(input())
a = permutations(range(1, n+1))

for i in a:
    print(' '.join(map(str, i)))
