n = list(input())
a = []
for i in range(len(n)):
    if ord(n[i]) < 97:
        a.append(ord(n[i])-64+26)
    else:
        a.append(ord(n[i])-96)
b = sum(a)
c = 0

for i in range(1, int(b**0.5)+1):
    if b % i == 0:
        c += 1

if c > 1:
    print("It is not a prime word.")
else:
    print("It is a prime word.")