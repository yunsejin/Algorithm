N = int(input().strip())
sudle = []

for _ in range(N):
    su = list(map(int, input().split()))
    sudle.append(su)

# 회의 시간 정렬 (끝나는 시간 기준, 같으면 시작 시간 기준)
sudle.sort(key=lambda x: (x[1], x[0]))

# 가능한 회의 선택
last_end_time = 0
count = 0
for start, end in sudle:
    if start >= last_end_time:
        count += 1
        last_end_time = end

# 결과 출력
print(count)