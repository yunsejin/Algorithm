import sys

input = sys.stdin.readline
n = int(input())
files = [input().strip() for _ in range(n)]

pattern = []
for i in range(len(files[0])):
    char = files[0][i]
    same = all(file[i] == char for file in files)
    pattern.append(char if same else '?')

result = ''.join(pattern)
print(result)
