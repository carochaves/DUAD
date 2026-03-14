#Cree una función que acepte un string con palabras separadas por un guion y retorne un string igual pero ordenado alfabéticamente.
def abc_order(text):

    words = text.split("-")
    words.sort()
    return "-".join(words)

print(abc_order("manzana-pera-banano-papaya-maracuya-cas"))
