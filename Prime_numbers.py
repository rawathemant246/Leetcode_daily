

def find_primes(n):
    primes = []  # List to hold prime numbers
    for num in range(2, n + 1):  # Start from 2, the smallest prime number
        is_prime = True  # Assume num is prime until proven otherwise
        for i in range(2, int(num ** 0.5) + 1):  # Check factors up to the square root of num
            if num % i == 0:
                is_prime = False  # Found a divisor, num is not prime
                break  # No need to check further, break out of the inner loop
        if is_prime:  # If num is prime after checking possible divisors
            primes.append(num)
    return primes

# Example usage
n = 30
prime_numbers = find_primes(n)
print("Prime numbers up to", n, ":", prime_numbers)