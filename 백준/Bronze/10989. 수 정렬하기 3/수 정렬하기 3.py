import sys
input=sys.stdin.readline

a = int(input())
arr = [0]*10001
for i in range(a):
    arr[int(input())] += 1
for j in range(10001):
    if arr[j]:
        for _ in range(arr[j]):
            print(j)