def check_capacity(lessons, max_capacity, m):
    count = 0
    total = 0
    for lesson in lessons:
        if total + lesson > max_capacity:
            count += 1
            total = lesson
            if count > m:
                return False
        else:
            total += lesson
    return count + 1 <= m

def min_bluray_size(lessons, m):
    left = max(lessons)
    right = sum(lessons)
    answer = right
    while left <= right:
        mid = (left + right) // 2
        if check_capacity(lessons, mid, m):
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
    return answer

n, m = map(int, input().split())
lessons = list(map(int, input().split()))

print(min_bluray_size(lessons, m))