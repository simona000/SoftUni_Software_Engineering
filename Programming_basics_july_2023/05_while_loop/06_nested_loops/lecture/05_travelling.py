destination = input()
minimum_budget = float(input())

saved_money = 0
while destination != 'End':
    input_line = input()
    current_line = int(input_line)
    saved_money += current_line
    if saved_money >= minimum_budget:
        print(f'Going to {destination}')

    input_line = input()


