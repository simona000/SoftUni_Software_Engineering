import sys

input_line = input()
max_number = -sys.maxsize

while input_line != 'Stop':
    current_line = int(input_line)

    if current_line > max_number:
        max_number = current_line

    input_line = input()

print(max_number)
