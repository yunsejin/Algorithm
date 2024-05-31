def find_last_tidy_number(n):
    digits = list(str(n))
    length = len(digits)
    
    mark = length
    for i in range(length - 1, 0, -1):
        if digits[i] < digits[i - 1]:
            mark = i
            digits[i - 1] = str(int(digits[i - 1]) - 1)
    
    for i in range(mark, length):
        digits[i] = '9'
    
    return int("".join(digits))

def solve_tidy_numbers(test_cases):
    results = []
    for i, n in enumerate(test_cases):
        last_tidy = find_last_tidy_number(n)
        results.append(f"Case #{i + 1}: {last_tidy}")
    return results

T = int(input().strip())
test_cases = [int(input().strip()) for _ in range(T)]

results = solve_tidy_numbers(test_cases)

for result in results:
    print(result)
