import sys
input = sys.stdin.read

def main():
    data = input().split('\n')
    initial_string = data[0]
    commands_count = int(data[1])
    commands = data[2:2+commands_count]
    
    left_stack = list(initial_string)
    right_stack = []
    
    for command in commands:
        if command[0] == 'L' and left_stack:
            right_stack.append(left_stack.pop())
        elif command[0] == 'D' and right_stack:
            left_stack.append(right_stack.pop())
        elif command[0] == 'B' and left_stack:
            left_stack.pop()
        elif command[0] == 'P':
            left_stack.append(command[2])
            
    print(''.join(left_stack + right_stack[::-1]))

if __name__ == "__main__":
    main()