def triangle_type(a, b, c):
    sides = sorted([a, b, c])
    a, b, c = sides[0], sides[1], sides[2]
    
    if a + b <= c:
        return 0
    
    if a == b == c:
        return 2
    
    if a * a + b * b == c * c:
        return 1
    
    return 0

a, b, c = map(int, input().split())
print(triangle_type(a, b, c))
