Peter_budget = float(input())
videocards = int(input())
processors = int(input())
ram_storage = int(input())

videocards_price = videocards * 250
processors_price = videocards_price * 0.35 * processors
ram_storage_price = videocards_price * 0.1 * ram_storage

total_sum = videocards_price + processors_price + ram_storage_price

if videocards > processors:
   total_sum = total_sum * 0.85
diff = abs(total_sum - Peter_budget)

if Peter_budget >= total_sum:
    print(f'You have {diff:.2f} leva left!')
else:
    print(f'Not enough money! You need {diff:.2f} leva more!')



# money_left = Peter_budget - (total_sum -
# if discount <= Peter_budget:
#         print(f'You have {money_left} leva left!')

# final_sum = total_sum - discount
#
# if final_sum <= Peter_budget:
#         money_left = Peter_budget - total_sum
#         print(f'You have {money_left} leva left!')
# elif final_sum > Peter_budget:
#         print(f'Not enough money! You need {needed_money} leva more!')