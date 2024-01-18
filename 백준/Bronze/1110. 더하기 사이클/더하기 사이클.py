n = int(input())
temp = n
count = 0

while temp != n or count == 0:
    # 주어진 수의 각 자릿수를 구함
    a = temp // 10  # 십의 자릿수
    b = temp % 10   # 일의 자릿수

    # 새로운 수 생성
    c = (a + b) % 10
    temp = (b * 10) + c

    # 사이클 수 증가
    count += 1

print(count)
