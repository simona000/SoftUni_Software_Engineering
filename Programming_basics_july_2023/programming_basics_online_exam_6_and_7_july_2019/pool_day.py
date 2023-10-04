import math

people_count = int(input())
entry_price = float(input())
price_per_chair = float(input())
price_per_umbrella = float(input())

tax_everyone = people_count * entry_price
needed_chairs = math.ceil(people_count * 0.75)
needed_chairs_price = needed_chairs * price_per_chair
needed_umbrellas = math.ceil(people_count * 0.5)
needed_umbrellas_price = needed_umbrellas * price_per_umbrella

total_expenses = tax_everyone + needed_umbrellas_price + needed_chairs_price

print(f'{total_expenses:.2f} lv.')