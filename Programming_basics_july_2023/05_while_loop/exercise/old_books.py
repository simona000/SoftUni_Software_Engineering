wanted_book = input()

count = 0
is_found = False
current_book = input()
while current_book != 'No More Books':
    if current_book == wanted_book:
        is_found = True
        break

    count += 1
    current_book = input()

if is_found:
    print(f'You checked {count} books and found it.')
else:
    print(f'The book you search is not here!')
    print(f'You checked {count} books.')