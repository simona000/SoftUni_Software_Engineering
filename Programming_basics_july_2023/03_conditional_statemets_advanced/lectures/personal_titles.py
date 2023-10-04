age = float(input())
gender = input()

if gender == 'm':
    pass
    if age < 16:
        print('Master')
    elif age >= 16:
        print('Mr.')
elif gender == 'f':
    pass
    if age < 16:
        print('Miss')
    elif age >= 16:
        print('Ms.')