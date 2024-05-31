def calculate(a, b, operator):
    if operator == 0:
        return a + b
    elif operator == 1:
        return a - b
    elif operator == 2:
        return a * b
    elif operator == 3:
        if a < 0:
            return -(-a // b)
        else:
            return a // b

def backtrack(index, current_result, plus, minus, multiply, divide):
    global max_result, min_result
    
    if index == N:
        max_result = max(max_result, current_result)
        min_result = min(min_result, current_result)
        return
    
    if plus > 0:
        backtrack(index + 1, calculate(current_result, A[index], 0), plus - 1, minus, multiply, divide)
    if minus > 0:
        backtrack(index + 1, calculate(current_result, A[index], 1), plus, minus - 1, multiply, divide)
    if multiply > 0:
        backtrack(index + 1, calculate(current_result, A[index], 2), plus, minus, multiply - 1, divide)
    if divide > 0:
        backtrack(index + 1, calculate(current_result, A[index], 3), plus, minus, multiply, divide - 1)

N = int(input().strip())
A = list(map(int, input().strip().split()))
plus, minus, multiply, divide = map(int, input().strip().split())

max_result = -float('inf')
min_result = float('inf')

backtrack(1, A[0], plus, minus, multiply, divide)

print(max_result)
print(min_result)
