def css(data_structure):  # css = calculate_structure_sum
    sum_ = 0
    if isinstance(data_structure, int):
        sum_ += data_structure
    elif isinstance(data_structure, float):
        sum_ += data_structure
    elif isinstance(data_structure, str):
        sum_ += len(data_structure)
    elif isinstance(data_structure, list):
        for k in data_structure:
            sum_ += css(k)
    elif isinstance(data_structure, set):
        for k in data_structure:
            sum_ += css(k)
    elif isinstance(data_structure, tuple):
        for k in data_structure:
            sum_ += css(k)
    elif isinstance(data_structure, dict):
        for i, j in data_structure.items():
            sum_ += css(i)
            sum_ += css(j)
    return sum_


data_structure = [[1, 2, 3], {'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8}), "Hello",
                  ((), [{(2, 'Urban', ('Urban2', 35))}])]


res = css(data_structure)
print(res)


