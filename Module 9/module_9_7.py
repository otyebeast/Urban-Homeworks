def is_prime(func):
    def wrapper(*args, **kwargs):
        result_ = func(*args, **kwargs)
        is_prime = True
        for i in range(2, result_):
            if result_ % i == 0:
                is_prime = False
        if is_prime == True:
            print("Простое")
            return result_
        else:
            print('Составное')
            return result_

    return wrapper


@is_prime
def sum_three(*args):
    otvet = 0
    for arg in args:
        otvet += arg
    return otvet


result = sum_three(2, 3, 6)
print(result)

result = sum_three(3, 3, 3)
print(result)
