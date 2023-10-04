
CONSTANT_NUMBER = int(input())
total_number = 0

while True:
    current_number = int(input())
    total_number += current_number

    if total_number >= CONSTANT_NUMBER:
        print(total_number)
        break