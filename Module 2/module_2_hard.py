def key(number):
    pass_ = ''
    for i in range(1, number):
        for k in range(i + 1, number):
            if number % (i + k) == 0:
                pass_ += str(i) + str(k)
    return pass_

print('Введите число: ')
print(key(int(input())))