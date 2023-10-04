processor_price = float(input()) * 1.57
video_card_price = float(input()) * 1.57
ram_storage_price = float(input()) * 1.57

ram_store_count = int(input())
discount_percentage = float(input())

total_ram_price = ram_storage_price * ram_store_count
processor_price_discounted = processor_price - (processor_price * discount_percentage)
video_card_price_discounted = video_card_price - (video_card_price * discount_percentage)
total_amount = processor_price_discounted + video_card_price_discounted + total_ram_price

print(f'Money needed - {total_amount:.2f} leva.')
