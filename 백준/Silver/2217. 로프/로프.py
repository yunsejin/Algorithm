def max_weight_possible(n, weights):
    weights.sort(reverse=True)
    max_weight = 0
    for i in range(n):
        current_weight = weights[i] * (i + 1)
        if current_weight > max_weight:
            max_weight = current_weight
    return max_weight

n = int(input())
weights = []
for _ in range(n):
    weights.append(int(input()))

print(max_weight_possible(n, weights))