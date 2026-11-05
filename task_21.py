import time

def timing(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args,**kwargs)
        stop = time.perf_counter()

        itog_time = (stop - start) * 1000
        print(f"функция выполнилась за {itog_time} мс")
        return result
    return wrapper

@timing
def test_func():
    summ = 0
    i = 0
    while i < 10000:
        i += 1
        summ += 1

test_func()