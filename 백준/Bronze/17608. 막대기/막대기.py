n = int(input())
stack = []

for _ in range(n):
    h = int(input())

    while stack and stack[-1] <= h:
        stack.pop()
    stack.append(h)

print(len(stack))