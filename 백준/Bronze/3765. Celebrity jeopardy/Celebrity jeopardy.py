import sys
input = sys.stdin.read

def main():
    data = input().strip().split('\n')
    for line in data:
        print(line)

if __name__ == "__main__":
    main()
