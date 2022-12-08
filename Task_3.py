# Реализуйте декоратор logging, который будет отвечать за логирование функций.
# На экран выводится название функции и её документация.
# Если во время выполнения декорируемой функции возникла ошибка, то в файл function_errors.log
# записываются названия функции и ошибки.
#
# Также постарайтесь сделать так, чтобы программа не завершалась после обнаружения первой же ошибки,
# а обрабатывала все декорируемые функции и сразу записывала все ошибки в файл.
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

zerodiv()
varname()
correctly()

