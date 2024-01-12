a = [None]*9

for i in range(9):
    a[i] = int(input())

max_num = max(a)
max_index = a.index(max_num) + 1

print(max_num)
print(max_index)