book_pages = int(input())
pages_per_hour = int(input())
days_to_finish = int(input())

total_hours = book_pages // pages_per_hour

needed_hours = total_hours // days_to_finish

print(needed_hours)