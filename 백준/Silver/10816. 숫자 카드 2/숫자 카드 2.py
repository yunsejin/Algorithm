import bisect

N = int(input())
cards = sorted(map(int, input().split()))
M = int(input())
candidate = list(map(int, input().split()))

for target in candidate:
    left_index = bisect.bisect_left(cards, target)
    right_index = bisect.bisect_right(cards, target)
    count = right_index - left_index
    print(count, end=" ")