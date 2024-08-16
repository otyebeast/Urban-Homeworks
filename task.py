y = 'Пылесос'
print(y[:len(y)//2+len(y)%2])
print(y[:len(y)//2:])
print(y[:len(y)//2])



_str = 'абракадабра'
print(f'Количество букв в слове: {len(_str)}')

print(f'Целочисленная середина слова: {len(_str) // 2}. Срез: {_str[:len(_str) // 2]}')
print(f'Остаток от деления на 2: {len(_str) % 2}')
print(f'Середина слова округленная вверх: {len(_str) // 2 + len(_str) % 2}. Срез: {_str[:len(_str) // 2 + len(_str) % 2]}')


# task1
word = 'slovoslovo'
print(word[0:3])

#task2
word1 = 'slovoslovo'            # // war[start:stop:step]
print(word1[-3:])

#task3
word3 = 'slovoslovo'
if len(word3)>3:
    print(word3[1:-1:2])
else:
    print(word3)

#task4
word4 = 'ПылесоС'
print(word4[0]+word4[-2:0:-1]+word4[-1])

#task5
word5 = 'ПылесоС'

