days = int(input()) - 1
room_type = input()
rating = input()
price_room = 0

if room_type == 'room for one person':
    price_room = 18 * days
elif room_type == 'apartment':
    price_room = 25 * days
    if days < 10:
        price_room = price_room * 0.70
    elif 10 <= days < 15:
        price_room = price_room * 0.65
    elif days >= 15:
        price_room = price_room * 0.50

elif room_type == 'president apartment':
    price_room = 35 * days
    if days < 10:
        price_room = price_room * 0.90
    elif 10 <= days < 15:
        price_room = price_room * 0.85
    elif days >= 15:
        price_room = price_room * 0.80

price_diss = price_room * 0.9
price_tip = price_room * 1.25

if rating == 'positive':
    price_room = price_room * price_tip
    print(f'{price_tip:.2f}')

elif rating == 'negative':
    price_room = price_room * price_diss
    print(f'{price_diss:.2f}')

