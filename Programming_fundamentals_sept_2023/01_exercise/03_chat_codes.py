number = int(input())
message = ''

for i in range(number):
    number = int(input())
    if number == 88:
        print('Hello')
    elif number == 86:
        print('How are you?')
    elif number < 88:
        print('GREAT!')
    else:
        print('Bye.')