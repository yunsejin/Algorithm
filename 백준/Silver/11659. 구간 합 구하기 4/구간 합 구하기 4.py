import sys
input = sys.stdin.readline
a, b = map(int, input().split())
c = list(map(int, input().split()))
aa = len(c)
sum_arr = [0] * (aa+1)
for i in range(1, aa+1):
    sum_arr[i] = sum_arr[i-1] + c[i-1]
for i in range(b):
    d, e = map(int, input().split())
    print(sum_arr[e] - sum_arr[d-1])