fixed_digits = [9, 7, 8, 0, 9, 2, 1, 4, 1, 8]

last_digits = [int(input()) for _ in range(3)]

isbn_digits = fixed_digits + last_digits

total_sum = 0
for i in range(13):
    if i % 2 == 0:
        total_sum += isbn_digits[i] * 1
    else:
        total_sum += isbn_digits[i] * 3

print(f"The 1-3-sum is {total_sum}")
