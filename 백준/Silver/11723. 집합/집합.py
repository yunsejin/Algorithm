import sys

M = int(input())
S = 0

for _ in range(M):
    operation = sys.stdin.readline().strip().split()
    command = operation[0]

    if command in ['add', 'remove', 'check', 'toggle']:
        x = int(operation[1]) - 1

    if command == 'add':
        S |= (1 << x)
    elif command == 'remove':
        S &= ~(1 << x)
    elif command == 'check':
        print(1 if S & (1 << x) else 0)
    elif command == 'toggle':
        S ^= (1 << x)
    elif command == 'all':
        S = (1 << 20) - 1
    elif command == 'empty':
        S = 0
