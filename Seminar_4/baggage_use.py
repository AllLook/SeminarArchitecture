from SeminarArchitecture.Seminar_4.logistics_repository import Transport_company_repository


class Baggage():
    id_baggage: int
    id_user: Transport_company_repository.users
    weight: float
    description: str

    def __init__(self, id_baggage, id_user, weight, description):
        if id_baggage not in Transport_company_repository.users:
            self.id_baggage = id_baggage
        else:
            id_baggage += 1
            self.id_user = id_baggage
        self.weight = weight
        self.description = description

    def __str__(self):
        return f"Baggage: id_baggage: {self.id_baggage}, weight: {self.weight}, description: {self.description}"


if __name__ == '__main__':
    b1 = Baggage(1, 12.1, 'bla-bla-bla')
    Transport_company_repository.baggage[b1.id_baggage] = [b1.weight, b1.description]
    print(b1)
