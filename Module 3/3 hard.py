data_structure = [[1, 2, 3], {'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8}), "Hello",
                  ((), [{(2, 'Urban', ('Urban2', 35))}])]
list_2 = []
list_3 = []


def elements(data_structure):
    if isinstance(data_structure, (int, float)):
        list_3.append(data_structure)
    elif isinstance(data_structure, str):
        list_2.append(data_structure)
    elif isinstance(data_structure, list):
        for k in data_structure:
            elements(k)
    elif isinstance(data_structure, tuple):
        for k in data_structure:
            elements(k)
    elif isinstance(data_structure, set):
        for k in data_structure:
            elements(k)
    elif isinstance(data_structure, dict):
        for i, j in data_structure.items():
            elements(i)
            elements(j)


elements(data_structure)
print('Количество строк: ', len(list_2))
print('Сумма всех чисел: ', sum(list_3))

sum_ = 0
index = 0
while index < len(list_2):
    for i in list_2:
        sum_ = sum_ + len(i)
        index += 1

print('Общая сумма всех чисел и длины всех строк: ', sum(list_3) + sum_)
