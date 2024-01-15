n = int(input())

arr = []

a = input()
numbers = list(map(int, a.split()))

arr.extend(numbers)
min_value = min(arr)
max_value = max(arr)

print(min_value, max_value)
