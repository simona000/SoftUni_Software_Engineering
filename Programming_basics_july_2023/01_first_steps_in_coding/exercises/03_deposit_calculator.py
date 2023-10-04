deposit = float(input())
months = int(input())
annual_percentage = float(input())

per_year = deposit * (annual_percentage / 100)
per_month =  per_year/12

total_sum = deposit + (months * per_month)

print(total_sum)
