def min_bribes(votes):
    dasom_votes = votes[0]
    other_votes = votes[1:]

    bribes = 0

    if not other_votes:
        return 0

    while dasom_votes <= max(other_votes):
        max_votes = max(other_votes)
        max_index = other_votes.index(max_votes)
        other_votes[max_index] -= 1
        dasom_votes += 1
        bribes += 1

    return bribes

N = int(input())
votes = []

for i in range(N):
    votes.append(int(input()))

print(min_bribes(votes))