packages_of_pens = int(input())
packages_of_markers = int(input())
board_chemical = int(input())
discount = int(input())

price_pens = packages_of_pens * 5.80
price_markers = packages_of_markers * 7.20
price_chemical = board_chemical * 1.20

total = price_pens + price_markers + price_chemical

discount_price = total - (total * discount / 100)

print(discount_price)



