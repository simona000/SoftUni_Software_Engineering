type_screening = input()
rows = int(input())
columns = int(input())

income = 0

cinema_capacity = rows * columns

if type_screening == 'Premiere':
    income = cinema_capacity * 12.00
elif type_screening == 'Normal':
    income = cinema_capacity * 7.50
elif type_screening == 'Discount':
    income = cinema_capacity * 5.00

print(f'{income:.2f} leva')