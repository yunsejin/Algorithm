from itertools import combinations

def l():
    while True:
        a = input()
        if a == '0':
            break
        b = list(map(int, a.split()))[1:]
        
        for i in combinations(b, 6):
            print(' '.join(map(str, i)))
        print()

l()