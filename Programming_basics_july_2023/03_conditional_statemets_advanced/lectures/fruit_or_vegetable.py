# type_of_product = input()
#
# if type_of_product == 'banana' or type_of_product == 'apple' or type_of_product == 'kiwi' or type_of_product == 'cherry' or type_of_product == 'lemon' or type_of_product == 'grapes':
#     print('fruit')
# elif type_of_product == 'tomato' or type_of_product == 'cucumber' or type_of_product == 'pepper' or 'carrot':
#     print('vegetable')
# else:
#     print('unknown')

product = input()

fruits = ["banana" , "apple", "kiwi", "cherry", "lemon", "grapes"]

vegetables = ["tomato", "cucumber", "pepper", "carrot"]

if (product in fruits):
    print("fruit")
elif (product in vegetables):
    print("vegetable")
else:
    print("unknown")
