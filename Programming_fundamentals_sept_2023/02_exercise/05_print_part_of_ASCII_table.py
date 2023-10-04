first_line = int(input())
second_line = int(input())
for number in range(first_line, second_line + 1):
    if number == second_line:
        print(chr(number))
    else:
        print(chr(number), end=' ')