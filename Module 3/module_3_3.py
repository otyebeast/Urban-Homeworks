# def print_params(a, b, c):   #  *args, **kwargs
#     print(a, b, c)
#
# list_ = [1, 2]
# dict_ = {'c': 3}
# print_params(*list_, **dict_)

def print_params(a = 1, b = 'string', c = True):
    print(a, b, c)


values_list = [8, 'matrix', False]
values_dict = {'a': 9, 'b': 'xirtam', 'c': False}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [True, 'newest']

print_params(*values_list_2, 42)