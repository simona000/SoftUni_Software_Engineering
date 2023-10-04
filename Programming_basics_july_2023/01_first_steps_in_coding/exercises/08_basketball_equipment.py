annual_tax = int(input())

sneakers = annual_tax - (annual_tax * 0.4)
clothes = sneakers - (sneakers * 0.2)
ball = clothes / 4
accessories = ball / 5

total_expenses = annual_tax + sneakers + clothes + ball + accessories

print(total_expenses)