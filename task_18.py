import time

def log_calls(func):
    def wrapper(*args, **kwargs):
        with open("text.txt", "w") as file:
            file.write(f"data: {time.ctime()}\t")
            file.write(f"name: {func.__name__}\t")
            file.write(f"argument: {args}, {kwargs}\t")

        return func(*args, **kwargs)
    
    return(wrapper)

@log_calls
def function(word):
    print(word)

function("hello, how are you?")