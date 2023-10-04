students = int(input())

group_one = 0
group_two = 0
group_three = 0
group_four = 0

total_grades = 0
for i in range(1, students + 1):
    grade = float(input())

    if grade < 3.00:
        group_four += 1
    elif grade < 4.00:
        group_three += 1
    elif grade < 5.00:
        group_two += 1
    else:
        group_one += 1

    total_grades += grade

percentage_one = group_one / students * 100
percentage_two = group_two / students * 100
percentage_three = group_three / students * 100
percentage_four = group_four / students * 100

average_grade_total = total_grades / students
print(f'Top students: {percentage_one:.2f}%')
print(f'Between 4.00 and 4.99: {percentage_two:.2f}%')
print(f'Between 3.00 and 3.99: {percentage_three:.2f}%')
print(f'Fail: {percentage_four:.2f}%')
print(f'Average: {average_grade_total:.2f}')
