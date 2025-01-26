


def sieve_of_eratosthenes(n):
    is_prime = [True] * (n + 1)# Assume all numbers are prime initially
    print(len(is_prime))
    p = 2
    while (p * p <= n):
        if (is_prime[p] == True):  # If prime[p] is not changed, then it is a prime
            for i in range(p * p, n + 1, p):  # Updating all multiples of p to not prime
                is_prime[i] = False
        p += 1
    primes = [p for p in range(2, n + 1) if is_prime[p]]  # Collect all prime numbers
    return primes

# Example usage
n = 100
prime_numbers = sieve_of_eratosthenes(n)
print("Prime numbers up to", n, ":", prime_numbers)




