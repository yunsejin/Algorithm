def permute_unique(nums, path, result):
    if len(path) == M:
        result.append(path[:])
        return
    
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        path.append(nums[i])
        permute_unique(nums[:i] + nums[i+1:], path, result)
        path.pop()

N, M = map(int, input().split())
numbers = sorted(list(map(int, input().split())))
result = []
permute_unique(numbers, [], result)

for seq in result:
    print(' '.join(map(str, seq)))