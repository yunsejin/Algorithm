def solution(numbers):
    b = []
    b.append(max(numbers))
    numbers.remove(max(numbers))
    b.append(max(numbers))
    return b[0]*b[1]