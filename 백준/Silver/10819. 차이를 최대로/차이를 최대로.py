from itertools import permutations
n=int(input())
a=list(map(int,input().split()))
b=0
for j in permutations(a):
    p=0
    for i in range(1,len(j)):
        p+=abs(j[i]-j[i-1])
    if p>b:
        b=p
print(b)