a = int(input())

results = []
for i in range(1, a + 1):
    b, c = map(int, input().split())
    results.append(b + c)

for result in results:
    print(result)
