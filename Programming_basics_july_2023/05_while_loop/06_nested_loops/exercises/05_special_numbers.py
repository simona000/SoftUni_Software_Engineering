n = int(input())


for i in range(1, 10):
    for k in range(1,10):
        for l in range(1,10):
            for m in range(1,10):
                is_valid = n % i == 0 and n % k == 0 and n % l == 0 and n % m == 0
                if is_valid:
                    print(f'{i}{k}{l}{m}',end = ' ')