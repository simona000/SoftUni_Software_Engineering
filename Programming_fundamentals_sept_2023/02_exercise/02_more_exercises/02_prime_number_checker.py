input_number = int(input())

if input_number <= 1:
    is_prime = False
else:
    is_prime = True
    for i in range(2, int(input_number ** 0.5) + 1):
        if input_number % i == 0:
            is_prime = False
            break
print(is_prime)

