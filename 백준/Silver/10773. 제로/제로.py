import sys
input=sys.stdin.readline

n = int(input())

def zero(n):
    stack = []
    for _ in range(n):
        m = int(input())
        if(m == 0):
            stack.pop()
        else:
            stack.append(m)
    return  print(sum(stack))

zero(n)