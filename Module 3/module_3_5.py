def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])
    if len(str_number) > 1:
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        return first


result = get_multiplied_digits(40203)
print(result)



# def summa(n):
#     if n == 0:
#         return 0
#     else:
#         return n + summa(n - 1)
#
#
# print(summa(5))

# number = 01234  # leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
# str_ = str(number)
# int_ = int(str_[1:])
# print(int_)

# number = input()
# str_number = str(number)
# first = int(str_number[0])
# second = int(str_number[1])
# third = int(str_number[2])
# fourth = int(str_number[3])
# fifth = int(str_number[4])
# print(fifth + first + fourth + second + third)