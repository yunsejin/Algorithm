def backtrack(index, num_list, visited, signs, results):
    if index == len(signs) + 1:
        results.append("".join(map(str, num_list)))
        return
    
    for num in range(10):
        if not visited[num]:
            if index == 0 or (signs[index - 1] == '<' and num_list[-1] < num) or (signs[index - 1] == '>' and num_list[-1] > num):
                visited[num] = True
                num_list.append(num)
                backtrack(index + 1, num_list, visited, signs, results)
                num_list.pop()
                visited[num] = False

def find_max_min(k, signs):
    visited = [False] * 10
    max_results = []
    min_results = []
    
    backtrack(0, [], visited, signs, max_results)
    
    visited = [False] * 10
    
    backtrack(0, [], visited, signs, min_results)
    
    max_results.sort(reverse=True)
    min_results.sort()
    
    return max_results[0], min_results[0]

k = int(input().strip())
signs = input().strip().split()

max_value, min_value = find_max_min(k, signs)

print(max_value)
print(min_value)
