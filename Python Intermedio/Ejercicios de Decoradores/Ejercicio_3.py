from datetime import date


class User:

    def __init__(self, date_of_birth):
        self.date_of_birth = date_of_birth

    @property
    def age(self):

        today = date.today()

        return today.year - self.date_of_birth.year


def validate_age(func):

    def wrapper(user):

        if user.age < 18:
            raise Exception("El usuario es menor de edad")

        return func(user)

    return wrapper


@validate_age
def create_bank_account(user):
    print("Cuenta bancaria creada correctamente")


adult = User(date(2000, 5, 10))
minor = User(date(2012, 3, 20))

create_bank_account(adult)
create_bank_account(minor)