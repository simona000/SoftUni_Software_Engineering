n = int(input())

left_sum = 0
right_sum = 0

for i in range(1, n + 1):
    first_num = int(input())
    second_num = int(input())
    third_num = int(input())
    forth_num = int(input())
    left_sum += first_num + second_num
    right_sum += third_num + forth_num
    if right_sum == left_sum:
        # total_sum = left_sum + right_sum
        print(f'Yes, sum = {left_sum}')
    else:
        diff = abs(left_sum - right_sum)
        print(f'No, diff = {diff}')