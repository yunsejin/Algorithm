import sys
input = sys.stdin.readline
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
for i in range(len(a)):
    if a[i] == 0:
        print(f"Case #{i+1}: INSOMNIA")
    else:
        s = set()
        j = 1
        while True:
            s.update(str(a[i]*j))
            if len(s) == 10:
                print(f"Case #{i+1}: {a[i]*j}")
                break
            j += 1