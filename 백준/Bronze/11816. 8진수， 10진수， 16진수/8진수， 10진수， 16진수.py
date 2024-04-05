import sys
input = sys.stdin.readline
a = input()
b = list(a)
if b[0] == '0' and b[1] == 'x':
    print(int(a, 16))
elif b[0] == '0':
    print(int(a, 8))
else:
    print(int(a))