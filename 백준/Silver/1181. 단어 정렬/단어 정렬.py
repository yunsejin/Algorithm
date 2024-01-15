a = int(input())
b = []

for i in range(1, a+1):
    c = input()
    b.append((c, len(c)))

def custom_sort(item):
    return (item[1], item[0])

b.sort(key=custom_sort)

unique_words = set()
result = []

for word, length in b:
    if word not in unique_words:
        unique_words.add(word)
        result.append(word)

for word in result:
    print(word)
