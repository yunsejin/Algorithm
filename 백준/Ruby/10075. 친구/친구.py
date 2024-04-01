n = int(input())
trust = list(map(int, input().split()))
protocols = list(map(int, input().split()))

friends = [set() for _ in range(n)]

for i in range(1, n):
    host = protocols[2 * (i - 1)]
    protocol = protocols[2 * (i - 1) + 1]
    if protocol == 0:
        friends[host].add(i)
        friends[i].add(host)
    elif protocol == 1:
        for friend in list(friends[host]):
            friends[friend].add(i)
            friends[i].add(friend)
    elif protocol == 2:
        for friend in list(friends[host]):
            friends[friend].add(i)
            friends[i].add(friend)
        friends[host].add(i)
        friends[i].add(host)

max_trust = 0
for i in range(1 << n):
    sample = set()
    sample_trust = 0
    for j in range(n):
        if i & (1 << j):
            if any(friend in sample for friend in friends[j]):
                break
            sample.add(j)
            sample_trust += trust[j]
    max_trust = max(max_trust, sample_trust)

print(max_trust)