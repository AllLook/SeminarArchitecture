from datetime import datetime

from SeminarArchitecture.Seminar_4.logistics_repository import Transport_company_repository
from SeminarArchitecture.Seminar_4.user import User


class Ticket:
    i: int
    id_ticket: int
    global id_bus
    data_ticket: datetime
    price: float
    place: int
    global active
    id_user = User.id_user

    if len(Transport_company_repository.id_bus) > 0: #если есть доступный автобус
        active = True
        id_bus = Transport_company_repository.id_bus[i]
    else:
        active = False

    def __init__(self, id_ticket, id_user, id_bus, data_ticket, price, place, active):
        if id_ticket not in Transport_company_repository.ticket:
            self.id_ticket = id_ticket
        else:
            id_ticket += 1
            self.id_ticket = id_ticket
        self.id_user = id_user
        self.id_bus = id_bus
        self.data_ticket = data_ticket
        self.price = price
        self.place = place
        self.active = active

    def __str__(self):
        return f"Ticket: id_ticket: {self.id_ticket}, data_ticket: {self.data_ticket}, price: {self.price}, active: {self.active}"


if __name__ == '__main__':
    t1 = Ticket(1, 2, 3, datetime.now(), 150.5, 5, active)
    Transport_company_repository.users[t1.id_ticket] = [t1.id_user, t1.id_bus, t1.data_ticket, t1.price, t1.active]
    print(t1)
