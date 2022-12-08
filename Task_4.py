# При моделировании компьютерных объектов используются два типа фигур:
# прямоугольники и квадраты. Каждая из них имеет координаты XY, длину и ширину.
# Также каждая фигура может менять координаты (двигаться) и менять размер.
#
# Реализуйте такие классы. Учтите, что с точки зрения интерфейса прямоугольник и квадрат
# — это разные фигуры и работают они по-разному. В частности, по разному работает метод изменения размера фигуры,
# так как у квадрата все стороны равны.

class Figure:

    def __init__(self, pos_x, pos_y, length, width):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.length = length
        self.width = width

    def move(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y


class ResizeAbleMixin:
    def resize(self, length, width):
        self.length = length
        self.width = width


class Rectangle(Figure, ResizeAbleMixin):
    pass


class Square(Figure, ResizeAbleMixin):

    def __init__(self, pos_x, pos_y, size):
        super().__init__(pos_x, pos_y, size, size)
