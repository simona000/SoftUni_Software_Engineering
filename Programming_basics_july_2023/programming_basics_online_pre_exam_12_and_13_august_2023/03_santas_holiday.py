days = int(input())
room = input()
evaluation = input()
price = 0
nights = days - 1
if days <= 10:
    if room == "room for one person":
        price = nights*18.00
    elif room == "apartment":
        price = 0.7*(nights*25.00)
    elif room == "president apartment":
        price = 0.9*(nights*35)
if 10 < days <= 15:
    if room == "room for one person":
        price = nights*18.00
    elif room == "apartment":
        price = 0.65*(nights*25.00)
    elif room == "president apartment":
        price = 0.85*(nights*35)
if days > 15:
    if room == "room for one person":
        price = nights*18.00
    elif room == "apartment":
        price = 0.5*(nights*25.00)
    elif room == "president apartment":
        price = 0.8*(nights*35)
if evaluation == "positive":
    price = price + 0.25*price
elif evaluation == "negative":
    price = price - 0.1*price
print("%.2f" % price)


























# days_count = int(input()) - 1
# room_type = input()
# review = input()
#
# price = -
#
# if room_type == 'room for one person':
#     room_for_one_price = 18.00 * days_count
# elif room_type == 'apartment':
#     apartment_price = 25.00 * days_count
#     if days_count < 10:
#         apartment_price = apartment_price * 0.70
#     elif 10 < days_count <= 15:
#         apartment_price = apartment_price * 0.65
#     elif days_count > 15:
#         apartment_price = apartment_price * 0.50
# elif room_type == 'president apartment':
#     president_apartment_price = 35.00 * days_count
#     if days_count < 10:
#         president_apartment_price = president_apartment_price * 0.90
#     elif 10 < days_count <= 15:
#         president_apartment_price = president_apartment_price * 0.85
#     elif days_count > 15:
#         president_apartment_price = president_apartment_price * 0.80
#
# if review == 'positive' and room_type == 'apartment':
#     apartment_price = apartment_price *
#
# # if review == 'positive':
# #     if room_type == 'apartment':
# #         apartment_price = apartment_price * 0.75
# #     elif room_type == 'president apartment':
# #         president_apartment_price = president_apartment_price * 0.75
# # elif review == 'negative':
# #     if room_type == 'apartment':
# #         apartment_price = apartment_price * 0.90
# #     elif room_type == 'president apartment':
# #         president_apartment_price = president_apartment_price * 0.90
# #
# # if room_type == 'apartment':
# #     print(f'{apartment_price:.2f}')
# # elif room_type == 'president apartment':
# #     print(f'{president_apartment_price:.2f}')
# # elif room_type == 'room for one person':
# #     print(f'{room_for_one_price:.2f}')