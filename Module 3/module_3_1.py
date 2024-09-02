calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string):
    count_calls()
    return len(string), string.upper(), string.lower()


def is_contains(string, list_to_search):
    count_calls()
    return string.casefold() in [s.casefold() for s in list_to_search]


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycle', 'cyclic']))
print(calls)



# a = 5
# b = 10
# def printer():
#     global a, b
#     a = 'Str'
#     b = 'Str2'
#     c = 15
#     d = 20
#     print(c, d, 'local')
#     print(a, b, 'global')
#
#
# print(a, b)
# printer()
# print(a, b)
# print(a, b)
# print(a, b)
# print(a, b)