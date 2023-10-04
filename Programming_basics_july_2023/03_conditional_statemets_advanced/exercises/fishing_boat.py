budget_all = int(input())
season = input()
man_count = int(input())

rent_price = 0

if season == 'Spring':
    rent_price = 3000
elif season == 'Summer' or season == 'Autumn':
    rent_price = 4200
elif season == 'Winter':
    rent_price = 2600

if man_count <= 6:
    rent_price = rent_price * 0.90
elif 6 < man_count <= 11:
    rent_price = rent_price * 0.85
elif man_count > 11:
    rent_price = rent_price * 0.75

if man_count % 2 == 0 and season != 'Autumn':
    rent_price = rent_price * 0.95

diff = abs(budget_all - rent_price)

if budget_all >= rent_price:
    print(f'Yes! You have {diff:.2f} leva left.')
else:
    print(f'Not enough money! You need {diff:.2f} leva.')