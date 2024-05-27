def check_gnomes_order(n, groups):
    results = ["Gnomes:"]
    for group in groups:
        if group == sorted(group) or group == sorted(group, reverse=True):
            results.append("Ordered")
        else:
            results.append("Unordered")
    return results

N = int(input())
groups = [list(map(int, input().split())) for _ in range(N)]

results = check_gnomes_order(N, groups)

for result in results:
    print(result)
