n = int(input())

if n == 1:
    print("*")
for i in range(1, n):
    if i == 1:
        print(" "*(n-1)+"*")
    if i < n-1:
        print(" "*(n-i-1)+"*"+" "*(i*2-1)+"*")
    else:
        print("*"*(n+n-1))