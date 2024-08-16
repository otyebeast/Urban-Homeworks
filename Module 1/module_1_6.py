# hone_book = {'Denis': 88005553535, 'Max': 88005553534}
# phone_book['Denis'] = 15123123123
# phone_book['Anton'] = 12324353445
# phone_book.update({'Sasha': 324532534435,
#                    'Alex': 5456234634})
# print(phone_book.get('Dima', 'Такого номера не существует'))
# print(phone_book)
# a = phone_book.pop('Max')
# print(phone_book)
# print(a)
# print(phone_book.keys())
# print(phone_book.values())
# print(phone_book.items())

# set_ = {1, 2, 3 , 5, 1, 8, 3, 'String', True, (1, 2, 3)}
# list_ = [1, 2, 1, 2, 1, 3, 2, 2]
# list_ = set(list_)
# print(list_.add(2))
# print(list_)
# print(set_)

my_dict = {'Albert': 1998, 'Alex': 2001, 'Alexey': 1999}
print(my_dict)
print(my_dict['Alex'])
print(my_dict.get('Egor'))
my_dict.update({'Egor': 1990,
                'Semen': 2000})
egor = my_dict.pop('Albert')
print(egor)
print(my_dict)

my_set = {8, 'Film', 1.5, True, 'Serial', 'Film', 8, 1.5}
print(my_set)
my_set.update({2, 'Mult'})
my_set.discard(8)
print(my_set)