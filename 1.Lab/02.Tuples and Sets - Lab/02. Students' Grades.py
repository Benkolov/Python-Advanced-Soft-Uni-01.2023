n = int(input())
student_records = {}

for i in range(n):
    name, grade = input().split()
    grade = float(grade)
    if name in student_records:
        student_records[name].append(grade)
    else:
        student_records[name] = [grade]

for name, grades in student_records.items():
    avg_grade = sum(grades) / len(grades)
    grades_str = " ".join(format(grade, ".2f") for grade in grades)
    print(f"{name} -> {grades_str} (avg: {avg_grade:.2f})")

