# from time import sleep
#
# a = 5
# print(a)
# print('Я тут')
# sleep(4)
# print('Фух, 4 секунды прошло')

# print('Hi, PyCharm')
# x = 43
# y = 32
# print(x * y)
# print("End Line")

# name = input('Введите ваше имя: ')
# if name == 'admin':
#     print('Hello, admin')
# else:
#     print('Hello'+',', name)

number = int(input('Enter number: '))  # Fizz, Buzz, FizzBuzz
if number % 3 == 0 and number % 5 == 0:
    print('Fizzbuzz')
elif number % 3 == 0:
    print('Fizz')
elif number % 5 == 0:
    print('Buzz')
else:
    print('Wrong number')
