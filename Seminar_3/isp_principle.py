from abc import ABC, abstractmethod


class Shape_rectangle(ABC):
    @abstractmethod
    def area(self, length, width):
        pass


class Shape_square(ABC):
    @abstractmethod
    def area(self, side):
        pass


class Area_rectangle(Shape_rectangle):
    length: float
    width = float

    def area(self, length, width):
        self.length = length
        self.width = width
        return length * width


class Area_square(Shape_square):
    side = float

    def area(self, side):
        self.side = side
        return side ** 2

if __name__ == '__main__':
    r = Area_rectangle()
    s = Area_square()
    print(r.area(12.3, 11.0))
    print(s.area(46))
