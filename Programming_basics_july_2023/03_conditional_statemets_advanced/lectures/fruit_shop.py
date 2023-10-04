product = input()
current_day = input()
quantity = float(input())
price_product = 0
wrong_data = False

if current_day == 'Monday' or current_day == 'Tuesday' or current_day == 'Wednesday' or current_day == 'Thursday' or current_day == 'Friday':
    if product == 'banana':
        price_product = 2.50
    elif product == 'apple':
        price_product = 1.20
    elif product == 'orange':
        price_product = 0.85
    elif product == 'grapefruit':
        price_product = 1.45
    elif product == 'kiwi':
        price_product = 2.70
    elif product == 'pineapple':
        price_product = 5.50
    elif product == 'grapes':
        price_product = 3.85
    else:
        wrong_data = True

elif current_day == 'Saturday' or current_day == 'Sunday':
    if product == 'banana':
        price_product = 2.70
    elif product == 'apple':
        price_product = 1.25
    elif product == 'orange':
        price_product = 0.90
    elif product == 'grapefruit':
        price_product = 1.60
    elif product == 'kiwi':
        price_product = 3.00
    elif product == 'pineapple':
        price_product = 5.60
    elif product == 'grapes':
        price_product = 4.20
    else:
        wrong_data = True
else:
    wrong_data = True

total_price = price_product * quantity

if wrong_data:
    print('error')
else:
    print(f"{total_price:.2f}")