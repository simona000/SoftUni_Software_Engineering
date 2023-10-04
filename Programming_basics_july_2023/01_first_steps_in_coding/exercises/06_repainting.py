needed_nylon = int(input())
needed_paint = int(input())
needed_thinner = int(input())
total_hours_to_finish = int(input())

nylon_price = (needed_nylon + 2) * 1.50
paint_price = (needed_paint + 1.1) * 14.50
thinner_price = needed_thinner * 5.00
bag_price = 0.40

price_of_materials = nylon_price + paint_price + thinner_price + bag_price
labor_price_per_hour = price_of_materials * 30 / 100
price_of_labor = labor_price_per_hour * total_hours_to_finish

total_sum = price_of_labor + price_of_materials

print(total_sum)

# labor_price_per_hour = nylon_price + paint_price + thinner_price * (30 / 100)
