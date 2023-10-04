sea_excursion_package = int(input())
mountain_excursion_package = int(input())
counter = sea_excursion_package + mountain_excursion_package
price = 0
earning = 0
while counter != 0:
    input_line = input()
    if input_line == 'sea':
        price = 680
        earning += 680
        sea_excursion_package -= 1
        counter -= 1

    elif input_line == 'mountain':
        price = 499
        earning += 499
        mountain_excursion_package -= 1
        counter -= 1
