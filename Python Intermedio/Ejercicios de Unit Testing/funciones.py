# Cree una función que retorne la suma de todos los números de una lista.

list_1 = [20, 30, 40, 50]

def total_sum():
    return sum(list_1)


# Cree una función que le dé la vuelta a un string y lo retorne.

def turn_over(my_string):
    reversed_string = ""

    for i in range(len(my_string) - 1, -1, -1):
        reversed_string += my_string[i]

    return reversed_string


# Cree una función que imprima el número de mayúsculas y el número de minúsculas en un string.

def total_upper_lower(my_string):
    upper = 0
    lower = 0

    for char in my_string:
        if char.isupper():
            upper += 1
        if char.islower():
            lower += 1

    return lower, upper


# Cree una función que acepte un string con palabras separadas por un guion y retorne un string igual pero ordenado alfabéticamente.

def abc_order(text):
    words = text.split("-")
    words.sort()
    return "-".join(words)


# Cree una función que acepte una lista de números y retorne una lista con los números primos de la misma.

def is_prime(number):
    if number <= 1:
        return False

    for div in range(2, number):
        if number % div == 0:
            return False

    return True


def prime_numbers(numbers_list):
    prime = []

    for number in numbers_list:
        if is_prime(number):
            prime.append(number)

    return prime


if __name__ == "__main__":

    print(f"La suma de la lista es {total_sum()}")

    print(turn_over("Costa Rica"))

    lower, upper = total_upper_lower("Me gusta el color AZUL")
    print(
        f'Tenemos: "Me gusta el color AZUL". '
        f'La cantidad de minúsculas es: {lower} '
        f'y de mayúsculas es: {upper}'
    )

    print(abc_order("manzana-pera-banano-papaya-maracuya-cas"))

    print(prime_numbers([2, 3, 4, 5, 6, 9, 11, 13, 139]))