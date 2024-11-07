def is_prime(func):
    def wrapper(*args, **kwargs):
        result_ = func(*args, **kwargs)
        for i in range(2, result_):
            if result_ % i == 0 and i != result_:
                print("Составное")
                return result_
            else:
                print('Простое')
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
