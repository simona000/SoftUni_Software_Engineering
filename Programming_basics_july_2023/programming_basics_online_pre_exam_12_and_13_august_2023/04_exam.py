students = int(input())

group_one = 0
group_two = 0
group_three = 0
group_four = 0

total_grades = 0
for i in range(1, students + 1):
    input_line = float(input())
    grade = float(input_line)

    if 5.00 > grade:
        group_one += 1
    elif 4.00 <= grade <= 4.99:
        group_two += 1
    elif 3.00 <= grade <= 3.99:
        group_three += 1
    elif grade < 3.00:
        group_four += 1
    total_grades += grade

percentage_one = group_one / 10 * 100
percentage_two = group_two / 10 * 100
percentage_three = group_three / 10 * 100
percentage_four = group_four / 10 * 100

average_grade_total = total_grades / 10
print(f'Top students: {percentage_one}%')
print(f'"Between 4.00 and 4.99: {percentage_two}%')
print(f'"Between 3.00 and 3.99: {percentage_three}%')
print(f'Fail: {percentage_three}%')
print(f'"Average: {average_grade_total:.2f}')


