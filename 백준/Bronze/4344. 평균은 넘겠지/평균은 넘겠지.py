a = int(input())

for _ in range(a):
    b = list(map(int, input().split()))
    total_scores = sum(b[1:])
    average_score = total_scores / b[0]
    
    above_average_count = 0
    for score in b[1:]:
        if score > average_score:
            above_average_count += 1
    
    percentage_above_average = (above_average_count / b[0]) * 100
    formatted_percentage = '{:.3f}%'.format(percentage_above_average)
    
    print(formatted_percentage)
