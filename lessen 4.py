# Реализуйте функцию in_dir, которая принимает в качестве аргумента путь
# и временно меняет текущую рабочую директорию на новую. Функция должна быть контекст-менеджером.
# Также реализуйте обработку ошибок (например, если такого пути не существует).
# Вне зависимости от результата выполнения контекст-менеджера нужно возвращаться в изначальную рабочую директорию.
#
#
#
# Пример основного кода:
#

# Результат:
#
# <тут все папки из вашего диска C>
from collections.abc import Iterator
from contextlib import contextmanager
import os

# @contextmanager
# def in_dir(path):
#     cur_path = os.getcwd()
#     os.chdir(path)
#     try:
#         yield
#     finally:
#         os.chdir(cur_path)
#
# with in_dir('C://'):
#     print(os.listdir())
os.chdir('C://')
with open("TNT.txt", 'w') as f:
    f.write('Hello')