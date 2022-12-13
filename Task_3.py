# Реализуйте декоратор logging, который будет отвечать за логирование функций.
#
# Дополнительно: запишите дату и время возникновения ошибки, используя модуль datetime.

import datetime
import os
from typing import Callable, Any


def logging(func: Callable) -> Callable:
    """Декоратор, который отвечает за логирование функций."""

    from datetime import datetime
    def wrapped_func(*args, **kwargs) -> Any:
        try:
            print('{name}: {docs}'.format(name=func.__name__, docs=func.__doc__))
            func(*args, **kwargs)

        except Exception as err:
            err = f'{datetime.now().strftime("%d.%m.%Y %H:%M:%S")}: {func.__name__}: {err}\n'
            with open('function_errors.log', 'a', encoding='utf-8') as file_error:
                file_error.write(err)

    return wrapped_func

@logging
def zerodiv() -> None:
    """ It is ZeroDivisionError"""
    x = 1 / 0


@logging
def varname() -> None:
    """ It is NameError"""
    x = y

@logging
def correctly() -> Any:
    """ It is correctly!"""
    x = 'Hello World!'
print('Hello')
zerodiv()
varname()
correctly()

