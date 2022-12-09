n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()
total_score = float()
for grade in student_marks[query_name]:
    total_score += grade
average_score = total_score / len(student_marks[query_name])
print(f"{average_score:.2f}")