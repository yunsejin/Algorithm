def solution(array, n):
    closest_value = array[0]
    smallest_difference = abs(n - array[0])
    
    for value in array:
        current_difference = abs(n - value)
        if current_difference < smallest_difference or (current_difference == smallest_difference and value < closest_value):
            closest_value = value
            smallest_difference = current_difference
            
    return closest_value