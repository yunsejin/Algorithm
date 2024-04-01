n = int(input())
a = list(map(int,input().split()))
if n==1:
    print(max(a)**2)
else:
    a.sort()
    print(a[-1]*a[0])