t_shirt_price = float(input())
needed_amount_for_free_ball = float(input())

shorts_price = t_shirt_price * 0.75
socks_price = shorts_price * 0.20
shoes_price = (shorts_price + t_shirt_price) * 2
total_amount = shorts_price + socks_price + shoes_price + t_shirt_price

discounted_amount = total_amount * 0.85

if discounted_amount >= needed_amount_for_free_ball:
    print(f'Yes, he will earn the world-cup replica ball!')
    print(f'His sum is {discounted_amount:.2f} lv.')
else:
    diff = abs(needed_amount_for_free_ball - discounted_amount)
    print("No, he will not earn the world-cup replica ball.")
    print(f'He needs {diff:.2f} lv. more.')


