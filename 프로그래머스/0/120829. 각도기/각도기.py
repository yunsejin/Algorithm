def solution(angle):
    
    if angle == 90:
        angle = 2
    elif angle < 90:
        angle = 1
    elif angle == 180:
        angle = 4
    else:
        angle = 3
    
    return angle