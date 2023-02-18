def students_credits(*args):
    total_credits = 0
    courses = {}

    for arg in args:
        name, points, max_points, diyan_points = arg.split("-")
        points = int(points)
        max_points = int(max_points)
        diyan_points = int(diyan_points)
        diyan_credits = round(points * diyan_points / max_points, 1)
        total_credits += diyan_credits
        courses[name] = diyan_credits

    courses_sorted = sorted(courses.items(), key=lambda x: (-x[1], x[0]))
    courses_info = "\n".join([f"{name} - {points:.1f}" for name, points in courses_sorted])

    if total_credits >= 240:
        message = f"Diyan gets a diploma with {total_credits:.1f} credits."
    else:
        credits_needed = 240 - total_credits
        message = f"Diyan needs {credits_needed:.1f} credits more for a diploma."

    return f"{message}\n{courses_info}"


# print(
#     students_credits(
#         "Computer Science-12-300-250",
#         "Basic Algebra-15-400-200",
#         "Algorithms-25-500-490"
#     )
# )

print(
    students_credits(
        "Discrete Maths-40-500-450",
        "AI Development-20-400-400",
        "Algorithms Advanced-50-700-630",
        "Python Development-15-200-200",
        "JavaScript Development-12-500-480",
        "C++ Development-30-500-405",
        "Game Engine Development-70-100-70",
        "Mobile Development-25-250-225",
        "QA-20-300-300",
    )
)
