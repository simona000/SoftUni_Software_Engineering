lenght = int(input())
width = int(input())
high = int(input())
percentage = float(input())

total = lenght * width * high / 1000
acc_volume = total * (percentage / 100)

result = total - acc_volume

print(result)