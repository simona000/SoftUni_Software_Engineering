chicken_menu = int(input())
fish_menu = int(input())
vegeterian_menu = int(input())

price_of_chichen_menu = chicken_menu * 10.35
price_of_fish_menu = fish_menu * 12.40
price_of_vegeterian_menu = vegeterian_menu * 8.15

order_price = price_of_chichen_menu + price_of_fish_menu + price_of_vegeterian_menu
dessert_price = order_price * 0.2

delivery_price = 2.50
total_order = order_price + dessert_price + delivery_price

print(total_order)