N = input()

def cal_min(expression):
    parts = expression.split('-')
    total = sum(map(int, parts[0].split('+')))

    for part in parts[1:]:
        total -= sum(map(int, part.split('+')))

    return total

print(cal_min(N))