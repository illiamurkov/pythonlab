def cashe(func):
    cashe_slovar = {}

    def wrapper(*args, **kwargs):
        key = args + tuple(sorted(kwargs.items()))

        if key in cashe_slovar:
            print(f"берем из кэша: {key} {cashe_slovar[key]}")
            return cashe_slovar[key]

        else:
            result = func(*args, **kwargs)
            cashe_slovar[key] = result

            return result
    return wrapper

@cashe
def proverka(x, y):
    return x * y
    
result1 = proverka(7, 9)
print(f"результат: {result1}")

result2 = proverka(3, 5)
print(f"результат: {result2}")

result3 = proverka(7, 9)
print(f"результат: {result3}")