from datetime import datetime


def timestamp(func):
    def wrapper(*args, **kwargs):
        start = datetime.now()

        resultado = func(*args, **kwargs)

        end = datetime.now()
        print(f'-> {func.__name__} took {end-start} seconds.')
        return resultado

    return wrapper
