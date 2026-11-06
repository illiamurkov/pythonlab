def type(func):
    def wrapper(a, b):
        if not isinstance(a, int) or not isinstance(b, int):
            raise TypeError("оба аргумента должны быть int")
        return func(a, b)
    return wrapper

@type
def proverka(a, b):
    return a + b

print(proverka(5, 10))

print(proverka("d", 5))