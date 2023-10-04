price_per_kilo_vegetable = float(input())
price_per_kilo_fruits = float(input())
vegetable_kilos = int(input())
fruits_kilos = int(input())

earnings_vegetables = price_per_kilo_vegetable * vegetable_kilos
earnings_fruits = price_per_kilo_fruits * fruits_kilos
total_earnings = earnings_fruits + earnings_vegetables
total_earnings_euro = total_earnings / 1.94
print(f'{total_earnings_euro:.2f}')