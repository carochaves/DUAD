def validar_numeros(func):

    def wrapper(*args, **kwargs):

        for parametro in args:

            if not isinstance(parametro, (int, float)):
                raise Exception("Todos los parámetros deben ser números")

        return func(*args, **kwargs)

    return wrapper