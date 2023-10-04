whole_number = int(input())
bonus_points = 0

if whole_number <= 100:
    bonus_points = 5

elif whole_number <= 1000:
    bonus_points = whole_number * 0.2
else:
    bonus_points = whole_number * 0.1

if whole_number % 2 == 0:
        bonus_points = bonus_points + 1
if whole_number % 10 == 5:
        bonus_points = bonus_points + 2

print(bonus_points)
print(bonus_points + whole_number)

