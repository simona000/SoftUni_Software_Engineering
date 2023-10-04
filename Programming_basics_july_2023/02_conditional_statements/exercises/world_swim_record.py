record_in_seconds = float(input())
distance_in_meters = float(input())
seconds_for_1_meter = float(input())

need_to_swim = distance_in_meters * seconds_for_1_meter
added_time = distance_in_meters // 15
added_time_in_seconds = added_time * 12.5

total_time = (need_to_swim + added_time_in_seconds)
needed_time = abs(total_time - record_in_seconds)

if total_time < record_in_seconds:
    print(f'Yes, he succeeded! The new world record is {total_time:.2f} seconds.')
else:
    print(f'No, he failed! He was {needed_time:.2f} seconds slower.')