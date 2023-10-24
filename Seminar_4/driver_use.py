from SeminarArchitecture.Seminar_4.logistics_repository import Transport_company_repository


class Driver():
    id_driver: int
    id_bus: int
    name: str
    surname: str

    def __init__(self, id_driver, id_bus, name, surname):
        if id_driver not in Transport_company_repository.drivers:
            self.id_driver = id_driver
        else:
            id_driver += 1
            self.id_user = id_driver
        self.id_bus = id_bus
        self.name = name
        self.surname = surname

    def __str__(self):
        return f"Driver: id_driver: {self.id_driver}, id_bus: {self.id_bus}, name: {self.name}, surname: {self.surname}"


if __name__ == '__main__':
    d1 = Driver(1, 2, 'Ivan', 'Ivanov')
    Transport_company_repository.drivers[d1.id_driver] = [d1.id_bus, d1.name, d1.surname]
    print(d1)
