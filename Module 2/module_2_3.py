# while 1 > 0:
#     number = int(input('Enter your number: '))
#     if number % 2 == 0:
#         print('Number is even')
#         continue
#     else:
#         print('Number is odd')
#         break
# print('Out of cycle')

# Homework
my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
index = 0
while index < len(my_list) and my_list[index] >= 0:
    if my_list[index] > 0:
        print(my_list[index])
    index += 1

# my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
# index = 0
# while index < len(my_list):
#     if my_list[index] > 0:
#         print(my_list[index])
#     index += 1

# my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
# index = 0
# for index in my_list:
#     if index > 0:
#         print(index, end=" ")
