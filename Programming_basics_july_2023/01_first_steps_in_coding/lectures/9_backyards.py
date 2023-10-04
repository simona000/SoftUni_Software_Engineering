square_meters_for_landscaping = float(input())
price_for_whole_yard = square_meters_for_landscaping * 7.61
discount = price_for_whole_yard * 0.18
final_price = price_for_whole_yard - discount


print(f'the final price is: {final_price} lv.')
print(f'the discount is: {discount} lv.')
