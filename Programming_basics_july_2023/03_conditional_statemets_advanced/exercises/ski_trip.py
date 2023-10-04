month = input()
staying_days = int(input())
type_room = ''
rating = ''
price_per_night = 0

if type_room == 'room for one person':
    price_per_night = 18 * staying_days
elif type_room == 'apartment':
    price_per_night = 25 * staying_days
elif type_room == 'president apartment':
    price_per_night = 35 * staying_days

if staying_days < 10 and (type_room == 'apartment'):
    price_per_night = price_per_night * 0.70
elif 10 <= staying_days <= 15 and (type_room == 'apartment'):
    price_per_night = price_per_night * 0.65
elif staying_days > 15:
    price_per_night = price_per_night * 0.50

if staying_days < 10 and (type_room == 'president apartment'):
    price_per_night = price_per_night * 0.90
elif 10 <= staying_days <= 15 and (type_room == 'president apartment'):
    price_per_night = price_per_night * 0.85
elif staying_days > 15:
    price_per_night = price_per_night * 0.80

if rating == 'positive':
    pass