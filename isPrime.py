def is_prime():
    primes = []
    numbers = int(input('How many numbers would you like to know if are primes? '))
    for possiblePrime in range(2, numbers+1):
        isprime_ = True
        for num in range(2, possiblePrime):
            if possiblePrime % num == 0:
                isprime_ = False
        if isprime_:
            primes.append(possiblePrime)
    print(primes)


is_prime()