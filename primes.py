"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    if number_of_primes < 1:
        raise ValueError

    list = []
    not_prime = set()
    for i in range(2, 1000):
        if i not in not_prime:
            list.append(i)
            if len(list) == number_of_primes:
                break
            not_prime.update(j for j in range(i*i, 1001, i))

    return list[:number_of_primes]