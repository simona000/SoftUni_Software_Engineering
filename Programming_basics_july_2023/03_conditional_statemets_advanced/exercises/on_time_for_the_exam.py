exam_hour = int(input())
exam_min = int(input())
arrival_hour = int(input())
arrival_min = int(input())

exam_all_minutes = (exam_hour * 60) + exam_min
arrival_all_minutes = (arrival_hour * 60) + arrival_min
diff_min = abs(arrival_all_minutes - exam_all_minutes)

if arrival_all_minutes > exam_all_minutes:
    print('Late')
    if diff_min >= 60:
        hour = diff_min // 60
        minutes = diff_min % 60
        print(f'{hour}:{minutes:02d} hours after the start')
    else:
        print(f'{diff_min} minutes after the start')
elif arrival_all_minutes == exam_all_minutes or diff_min <= 30:
    print('On time')
    if diff_min > 0:
        print(f'{diff_min} minutes before the start')
else:
    print('Early')
    if diff_min >= 60:
        hour = diff_min // 60
        minutes = diff_min % 60
        print(f'{hour}:{minutes:02d} hours before the start')
    else:
        print(f'{diff_min} minutes before the start')