# В программировании иногда возникает ситуация, когда работу функции нужно замедлить.
# Типичный пример — функция, которая постоянно проверяет, изменились ли данные на веб-странице или её код.
#
# Реализуйте декоратор, который перед выполнением декорируемой функции ждёт несколько секунд.

import time
from typing import Callable, Any

def how_are_you(func: Callable) -> Callable:
    """Декоратор, замедляющий работу декорируемой функции"""

    def wrapped_func(*args, **kwargs) -> Any:
        time.sleep(2)
        result = func(*args, **kwargs)
        return result

    return wrapped_func

@how_are_you
def test(number: int) -> int:
    summ = number + number
    print('{number}+{number}='.format(number=number), summ)


test(2)