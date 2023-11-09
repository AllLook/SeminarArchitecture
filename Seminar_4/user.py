from SeminarArchitecture.Seminar_4.logistics_repository import Transport_company_repository


class User():
    id_user = int
    name: str
    surname: str
    password: str
    card_number: str

    def __init__(self, id_user, name, surname, password, card_number):

        if id_user not in Transport_company_repository.users:
            self.id_user = id_user
        else:
            id_user += 1
            self.id_user = id_user

        self.name = name
        self.surname = surname
        self.password = hash(password)
        self.card_number = card_number


    def __str__(self):
        return f"User: id_user: {self.id_user}, name: {self.name}, surname: {self.surname}, password: {self.password}, card_number: {self.card_number}"


if __name__ == '__main__':
    u1 = User(1, 'Ivan', 'Ivanov', '123er4567', '1234567890')
    Transport_company_repository.users[u1.id_user] = [u1.name,u1.surname,u1.password, u1.card_number]
    print(u1)
