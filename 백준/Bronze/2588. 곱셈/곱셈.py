num1 = int(input())
num2 = int(input())

result = num1 * (num2 % 10)
result1 = num1 * ((num2 // 10) % 10)
result2 = num1 * (num2 // 100)
result3 = num1 * num2

print(result)
print(result1)
print(result2)
print(result3)