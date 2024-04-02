def solution(num_list):
    answer = 0
    for i in num_list:
        if i != 1:
            while True:
                if i == 1:
                    break
                if i % 2 == 0:
                    i = i // 2
                    answer += 1
                else:
                    i = i - 1
    return answer