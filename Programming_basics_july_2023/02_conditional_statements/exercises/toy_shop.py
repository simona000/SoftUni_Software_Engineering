trip_price = float(input())
puzzles = int(input())
dolls = int(input())
teddy_bears = int(input())
minions = int(input())
trucks = int(input())

total_sum = (puzzles * 2.60) + (dolls * 3.00) + (teddy_bears * 4.10) + (minions * 8.20) + (trucks * 2.00)
total_toys = puzzles + dolls + teddy_bears + minions + trucks

if total_toys >= 50:
    total_sum = total_sum - (total_sum * 0.25)

total_sum = total_sum - (total_sum * 0.1)

diff = abs(total_sum - trip_price)

if total_sum >= trip_price:
    print(f'Yes! {diff:.2f} lv left.')
else:
    print(f'Not enough money! {diff:.2f} lv needed.')


