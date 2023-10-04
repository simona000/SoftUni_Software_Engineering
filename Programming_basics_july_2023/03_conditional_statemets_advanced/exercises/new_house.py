# "Roses", "Dahlias", "Tulips", "Narcissus" или "Gladiolus";

type_flower = input()
quantity = int(input())
budget = int(input())
price = 0

if type_flower == 'Roses':
    price = 5.00 * quantity
    if quantity > 80:
        price = price * 0.9
elif type_flower == 'Dahlias':
    price = 3.80 * quantity
    if quantity > 90:
        price = price * 0.85
elif type_flower == 'Tulips':
    price = 2.80 * quantity
    if quantity > 80:
        price = price * 0.85
elif type_flower == 'Narcissus':
    price = 3.00 * quantity
    if quantity < 120:
        price = price * 1.15
elif type_flower == 'Gladiolus':
    price = 2.50 * quantity
    if quantity < 80:
        price = price * 1.20

left_money = abs(price - budget)
if budget >= price:
    print(f'Hey, you have a great garden with {quantity} {type_flower} and {left_money:.2f} leva left.')
else:
    print(f'Not enough money, you need {left_money:.2f} leva more.')

