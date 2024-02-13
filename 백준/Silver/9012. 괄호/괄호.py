def is_valid_parenthesis(string):
  stack = []
  for char in string:
    if char == '(':
      stack.append(char)
    elif char == ')':
      if not stack:
        return False
      stack.pop()
  return not stack

t = int(input())
for _ in range(t):
  string = input()
  if is_valid_parenthesis(string):
    print("YES")
  else:
    print("NO")