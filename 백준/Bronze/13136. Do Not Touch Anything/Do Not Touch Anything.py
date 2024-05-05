import math
a,b,c = map(int,input().split())
d = math.ceil(a/c)*math.ceil(b/c)
print(d)