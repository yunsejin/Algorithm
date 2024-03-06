def solution(numbers, direction):
    answer = []
    if direction == 'right':
        for i in range(len(numbers)):
            answer.append(numbers[i-1])
    else:
        for i in range(1, len(numbers)):
            answer.append(numbers[i])
        answer.append(numbers[0])
    return answer