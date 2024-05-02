from functools import wraps
from datetime import datetime
import logging
logging.basicConfig(format='%(levelname)s -> %(message)s', level=logging.WARN)


def timestamp(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = datetime.now()

        resultado = func(*args, **kwargs)

        end = datetime.now()
        print(f'-> {func.__name__} took {end-start} seconds.')
        return resultado

    return wrapper


def type_check(func):
    @wraps(func)
    def wrapper(*args, **kwargs):

        params: dict = func.__annotations__
        params.pop('return')

        index = 1  # Começa do 1 pq o 0 é o self
        for name, param_type in params.items():
            value = args[index]

            if not isinstance(value, param_type):
                logging.warning(
                    "type_check: Param '%s' type expected '%s', got '%s'.",
                    name,
                    param_type.__name__,
                    type(value).__name__)

            index += 1

        return func(*args, **kwargs)

    return wrapper
