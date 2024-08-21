first = int(input('Enter 1st number: '))
second = int(input('Enter 2nd number: '))
third = int(input('Enter 3rd number: '))

if first == second == third:
    print(3)
elif first == second or second == third or third == first:
    print(2)
else:
    print(0)

# first = int(input('Enter 1st number: '))
# second = int(input('Enter 2nd number: '))
# third = int(input('Enter 3rd number: '))
#
# if first == second == third:
#     print(3)
# elif first == second:
#     print(2)
# elif second == third:
#     print(2)
# elif third == first:
#     print(2)
# else:
#     print(0)
