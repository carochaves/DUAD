class Person:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Person({self.name!r})"


class Bus:
    def __init__(self, max_passengers):
        self.max_passengers = max_passengers
        self.passengers = []

    def add_passenger(self, person):
        if not isinstance(person, Person):
            raise TypeError("El pasajero debe ser una instancia de Person")

    def add_passenger(self):
        if self.passengers < self.max_passengers:
            self.passengers += 1
            return True

        print("El bus está lleno.")
        return False

    def remove_passenger(self, person=None):
        if not self.passengers:
            print("No hay pasajeros para bajar.")
            return None

        if person is None:
            return self.passengers.pop()

        if not isinstance(person, Person):
            raise TypeError("El pasajero debe ser una instancia de Person")

        if person in self.passengers:
            self.passengers.remove(person)
            return person

        print("Ese pasajero no está en el bus.")
        return None

