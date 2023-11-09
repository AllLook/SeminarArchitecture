from abc import ABC, abstractmethod


class Logistics_work(ABC):
    @abstractmethod
    def get_user(self):
        pass

    @abstractmethod
    def get_driver(self):
        pass

    @abstractmethod
    def get_baggage(self):
        pass
    @abstractmethod
    def get_ticket(self):
        pass

    @abstractmethod
    def get_id_bus(self):
        pass

    @abstractmethod
    def set_user(self):
        pass

    @abstractmethod
    def set_driver(self):
        pass

    @abstractmethod
    def set_baggage(self):
        pass

    @abstractmethod
    def set_ticket(self):
        pass

    @abstractmethod
    def set_id_bus(self):
        pass