# 시험 점수 입력 받기
score = int(input())

# 성적 판별
if 90 <= score <= 100:
    grade = 'A'
elif 80 <= score < 90:
    grade = 'B'
elif 70 <= score < 80:
    grade = 'C'
elif 60 <= score < 70:
    grade = 'D'
else:
    grade = 'F'

# 성적 출력
print(grade)