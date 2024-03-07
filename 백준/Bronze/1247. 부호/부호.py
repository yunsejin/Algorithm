import sys
input = sys.stdin.readline
for i in range(3):
    b = int(input())
    a = []
    for j in range(b):
        a.append(int(input()))
    if sum(a) == 0:
        print('0')
    elif sum(a) > 0:
        print('+')
    else:
        print('-')