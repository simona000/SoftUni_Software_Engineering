money_as_strings = input().split(", ")
count_of_beggars = int(input())
money_as_integers = []

for current_money in money_as_strings:
    money_as_integers.append(int(current_money))

start_index = 0
final_sum = []

while start_index < count_of_beggars:
    current_beggar_sum = 0
    for current_index in range(start_index, len(money_as_integers), count_of_beggars):
        current_beggar_sum += money_as_integers[current_index]
    final_sum.append(current_beggar_sum)
    start_index += 1
print(final_sum)


