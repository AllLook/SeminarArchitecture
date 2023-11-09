from abc import ABC, abstractmethod
from time import sleep as ts


class Engine(ABC):
    @abstractmethod
    def start(self):
        pass


class Car:
    engine = Engine

    def __init__(self, engine: Engine):
        self.engine = engine

    def start(self):
        self.engine.start()


class Petrol_engine(Engine):
    def start(self):
        for i in range(1, 4):
            print(f'{i}...')
            ts(1)
        print('Взлетаем на бензине!')
        return 'Хьюстон, Взлет прошёл успешно!'


class Diesel_engine(Engine):
    def start(self):
        for i in range(1, 4):
            print(f'{i}...')
            ts(1)
        print('Взлетаем на дизеле!')
        return 'Хьюстон, Взлет прошёл успешно!'


if __name__ == '__main__':
    p = Petrol_engine()
    d = Diesel_engine()
    print(p.start())
    print(d.start())
