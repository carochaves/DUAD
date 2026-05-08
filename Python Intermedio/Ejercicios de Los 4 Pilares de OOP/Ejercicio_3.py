class Trabajador:
    def trabajar(self):
        print("Estoy trabajando")


class Estudiante:
    def estudiar(self):
        print("Estoy estudiando")


class Persona(Trabajador, Estudiante):
    pass