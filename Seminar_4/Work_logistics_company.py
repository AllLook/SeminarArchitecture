from SeminarArchitecture.Seminar_4.Ticket_use import Ticket
from SeminarArchitecture.Seminar_4.Work_logistics import Logistics_work
from SeminarArchitecture.Seminar_4.baggage_use import Baggage
from SeminarArchitecture.Seminar_4.driver_use import Driver
from SeminarArchitecture.Seminar_4.logistics_repository import Transport_company_repository
from SeminarArchitecture.Seminar_4.user import User


class Work_users_logistics(Logistics_work):
    users = Transport_company_repository.users
    user = User
    drivers = Transport_company_repository.drivers
    driver = Driver
    baggages = Transport_company_repository.baggages
    baggage = Baggage
    tickets = Transport_company_repository.tickets
    ticket = Ticket
    id_bus = Transport_company_repository.id_bus

    def set_user(self, users: dict, user):
        self.users = users
        self.user = user
        users[user.id_user] = user

    def get_user(self, users: dict):
        self.users = users
        print(users)

    def set_driver(self, drivers: dict, driver):
        self.drivers = drivers
        self.driver = driver
        drivers[driver.id_driver] = driver

    def get_driver(self, drivers: dict):
        self.drivers = drivers
        print(drivers)

    def set_baggage(self, baggages: dict, baggage):
        self.baggages = baggages
        self.baggage = baggage
        baggages[baggage.id_baggage] = baggage

    def get_baggage(self, baggages: dict):
        self.baggages = baggages
        print(baggages)

    def set_ticket(self, tickets: dict, ticket):
        self.tickets = tickets
        self.ticket = ticket
        tickets[ticket.id_baggage] = ticket

    def get_ticket(self, tickets: dict):
        self.tickets = tickets
        print(tickets)

    def set_id_bus(self, id_bus: list, i: int):
        self.id_bus = id_bus
        id_bus.append(i)

    def get_id_bus(self, id_bus: list):
        self.id_bus = id_bus
        print(id_bus)

