budget = float(input())
nights = int(input())
price_per_night = float(input())
additional_expenses_percentage = int(input())


staying_expenses_before_diss = nights * price_per_night
additional_expenses_sum = budget * additional_expenses_percentage / 100
total_sum_before_dis= staying_expenses_before_diss + additional_expenses_sum

if nights >= 7:
    price_per_night = price_per_night * 0.95
    total_sum_after_disscount = price_per_night * nights
    money_left = abs(total_sum_after_disscount + additional_expenses_sum - budget)

    print(f'Ivanovi will be left with {money_left:.2f} leva after vacation.')

