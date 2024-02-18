a , b = map(int,input().split())
a_1 = 1
a_2 = 1
a_3 = 1
for i in range(1,a+1):
    a_1 *= i
for i in range(1,b+1):
    a_2 *= i
for i in range(1,a-b+1):
    a_3 *= i


print(a_1 // (a_2 * a_3))