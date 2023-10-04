import math

name_of_series = input()
series_length = int(input())
break_time = int(input())

lunch_time = break_time / 8
relax_time = break_time / 4
free_time = break_time - lunch_time - relax_time
needed_time = abs(series_length - free_time)
rounded_time = math.ceil(needed_time)

if free_time >= series_length:
    print(f'You have enough time to watch {name_of_series} and left with {rounded_time} minutes free time.')
else:
    print(f"You don't have enough time to watch {name_of_series}, you need {rounded_time} more minutes." )