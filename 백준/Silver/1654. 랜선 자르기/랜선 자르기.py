n, m = map(int, input().split())
a = [int(input()) for _ in range(n)]

def is_possible(length):
    count = sum(x // length for x in a) 
    return count >= m

start, end = 1, max(a)
result = 0

while start <= end:
    mid = (start + end) // 2
    if is_possible(mid):
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)
