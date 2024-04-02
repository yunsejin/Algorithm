import sys
input = sys.stdin.readline

n = int(input())
students = [list(map(int, input().split())) for _ in range(n)] 

def find_winners(n, students):
    sorted_by_subjects = [
        sorted(students, key=lambda x: (-x[i], x[0])) for i in range(1, 5)
    ]
    winners = set()
    result = []
    for i in range(4):
        for student in sorted_by_subjects[i]:
            if student[0] not in winners:
                winners.add(student[0])
                result.append(student[0])
                break
    return result

print(*find_winners(n, students))