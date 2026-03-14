#Cree una función que acepte una lista de números y retorne una lista con los números primos de la misma.

def is_prime(number):
    if number <= 1:
        return False
    
    for div in range(2,number):
        if number % div == 0:
            return False
        
    return True

def prime_numbers(numbers_list):
    prime = []

    for number in numbers_list:
        if is_prime(number):
            prime.append(number)
            
    return prime

print(prime_numbers([2,3,4,5,6,9,11,13,139]))