from random import choice
from abc import ABC, abstractmethod


class ItemFabric(ABC):
    @abstractmethod
    def create_item(self):
        pass

    def open_reward(self):
        self.game_item = self.create_item()
        self.game_item.open()


class IGameItem(ABC):
    @abstractmethod
    def open(self):
        pass


class GoldReward(IGameItem):
    def open(self):
        print('Gold')


class GoldGenerator(ItemFabric):
    def create_item(self):
        print('Create new bag')
        return GoldReward()


class GemReward(IGameItem):
    def open(self):
        print('Gem')


class GemGenerator(ItemFabric):
    def create_item(self):
        print('Create new bag')
        return GemReward()


class SilverReward(IGameItem):  # добавлено
    def open(self):
        print('silver')


class SilverGenerator(ItemFabric):
    def create_item(self):
        print('Create new bag')
        return SilverReward()


class Nothing(IGameItem):  # добавлено
    def open(self):
        print('chest is empty, try again')


class NothingGenerator(ItemFabric):
    def create_item(self):
        print('Create empty bag')
        return Nothing()


# ДЗ. Добавить новые предметы. Сундуки с новыми предметами.

if __name__ == '__main__':
    # gold_generator = GoldGenerator()
    # gold_generator.open_reward()
    lst = [GoldGenerator(), GemGenerator(), SilverGenerator(), NothingGenerator()]
    for i in range(20):
        choice(lst).open_reward()
