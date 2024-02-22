n = int(input())
m = [] 

for i in range(n):
    age, name = input().split()
    age = int(age)
    m.append((age, name, i))

m.sort(key=lambda x: (x[0], x[2]))

for m in m:
    print(m[0], m[1])