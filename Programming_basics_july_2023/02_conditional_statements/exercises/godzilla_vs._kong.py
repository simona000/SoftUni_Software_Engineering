budget = float(input())
statists = int(input())
price_clothes_per_statists = float(input())

decor_amount = budget * 0.1
clothes_amount = price_clothes_per_statists * statists
if statists > 150:
    discount = clothes_amount * 0.1
    clothes_amount = price_clothes_per_statists * statists - discount
total_sum = decor_amount + clothes_amount

needed_money = abs(budget - total_sum)

if total_sum > budget:
     print('Not enough money!')
     print(f'Wingard needs {needed_money:.2f} leva more.')
elif total_sum <= budget:
    print('Action!')
    print(f'Wingard starts filming with {needed_money:.2f} leva left.')


