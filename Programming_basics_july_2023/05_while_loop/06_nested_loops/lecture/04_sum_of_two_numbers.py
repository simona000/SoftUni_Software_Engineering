start = int(input())
end = int(input())
magic_number = int(input())
counter = 0
break_condition = False

for x in range(start, end +1):
    for y in range(start, end +1):

        counter += 1

        if x + y == magic_number:
            print(f'Combination N:{counter} ({x} + {y} = {magic_number})')
            break_condition = True
            break
    if break_condition:
        break
else:
    print(f'{counter} combinations - neither equals {magic_number}')