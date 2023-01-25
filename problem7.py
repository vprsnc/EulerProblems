def is_prime(n):
    if n < 2: pass
    for i in range(2, int(n**0.5) + 1):    # prime always less sqrt(n)
        if n % i == 0:
            return False
    return True


def prime(we_need):
    num_primes = 0
    p = 1

    while num_primes < we_need:
        p += 1
        if is_prime(p):
            num_primes += 1
    return p

we_need = 10001
print(prime(we_need))
