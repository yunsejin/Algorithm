str = input()
d = ""
for i in str:
    if i.islower():
        d += i.upper()
    else:
        d += i.lower()
print(d)