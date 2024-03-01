def solution(numbers):
    a = 0.0
    for i in numbers:
        a += i
    return a / len(numbers)