import itertools

def tsp_bruteforce(n, w):
    cities = list(range(n))
    min_cost = float('inf')
    
    for perm in itertools.permutations(cities[1:]):
        current_cost = 0
        k = 0
        for i in perm:
            if w[k][i] == 0:
                break
            current_cost += w[k][i]
            k = i
        else:
            if w[k][0] != 0:
                current_cost += w[k][0]
                min_cost = min(min_cost, current_cost)
    
    return min_cost

n = int(input().strip())
w = [list(map(int, input().split())) for _ in range(n)]

result = tsp_bruteforce(n, w)
print(result)
