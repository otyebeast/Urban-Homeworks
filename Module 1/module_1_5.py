# food = ['apple', 'coconut', 'banana']
# print(food[0])
# food[0] = 'peach'
# print(food)
# food.append(True)
# print(food)
# food.extend(['string', 2])
# print(food)
# food.remove('peach')
# print(food)
# print('coconut' not in food)
# print(food[0:2:2])

# tuple_ = ([1, 2], 3, 4) + (1, 2)
# print(tuple_)
# tuple_[0][0] = 8
# print(tuple_)
# tuple_ = (1, 2) * 3
# print(tuple_)

immutable_var = 1, 'apple', 1.8, True
print(immutable_var)
# immutable_var[0][0] = 4 // Значения элементов кортежа неизменны и упорядочены, кроме моментов, когда в кортеже находится список, можно изменить только список в кортеже

mutable_list = [1, 'apple', 1.8, 4, True]
mutable_list.remove(1)
mutable_list.append('melon')
mutable_list.extend([2, 1.2, 'berry'])
mutable_list[1] = 'green apple'
mutable_list.remove(True)
print(mutable_list)
