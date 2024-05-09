nums = range(1, 100)


def isPrime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


prime = list(filter(isPrime, nums))
print(prime)
