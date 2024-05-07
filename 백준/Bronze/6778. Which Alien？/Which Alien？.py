a = int(input())
b = int(input())
c = []
if a >= 3 and b <= 4:
    c.append('TroyMartian')
if a <= 6 and b >= 2:
    c.append('VladSaturnian')
if a <= 2 and b <= 3:
    c.append('GraemeMercurian')
for i in c:
    print(i)