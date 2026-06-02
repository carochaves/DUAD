def debug(func):

    def wrapper(*args, **kwargs):

        print("Parámetros:", args, kwargs)

        resultado = func(*args, **kwargs)

        print("Retorno:", resultado)

        return resultado

    return wrapper


@debug
def describir_animal(nombre, tipo):
    return f"{nombre} es un {tipo}"


describir_animal("Max", "perro")