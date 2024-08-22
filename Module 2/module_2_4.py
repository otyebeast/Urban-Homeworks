# list_ = ['one', 'two', 'three']
#
# for i in range(len(list_)):
#     list_[i] = ':('
#
# print(list_)

# for i in range(1, 11):
#     for j in range(1, 11):
#         print(f'{i} x {j} = {i * j}')


# dict_ = {'a': 1, 'b': 2, 'c':3}
#
# for i, k in dict_.items():
#     print(i, k)

# Homework

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []

for i in numbers:
    for k in range(2, 16):
        if i % k == 0 and i != k:
            not_primes.append(i)
            break
        elif i == k:
            primes.append(i)
        else:
            continue

print('Primes:', primes)
print('Not Primes:', not_primes)
