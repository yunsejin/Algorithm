from itertools import permutations
n=int(input())
a=list(map(int,input().split()))
def c(a):
    b=0
    for i in range(1,len(a)):
        b+=abs(a[i]-a[i-1])
    return b
def d(a):
    m=0
    for j in permutations(a):
        p=c(j)
        m=max(m,p)
    return m
print(d(a))