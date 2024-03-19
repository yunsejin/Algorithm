dp_zero = [0] * 41
dp_one = [0] * 41

dp_zero[0] = 1
dp_one[1] = 1

for i in range(2, 41):
    dp_zero[i] = dp_zero[i-1] + dp_zero[i-2]
    dp_one[i] = dp_one[i-1] + dp_one[i-2]

T = int(input())
for _ in range(T):
    n = int(input())
    print(dp_zero[n], dp_one[n])
