

def linear_sieve(n):
    is_prime = [True] * (n + 1)  # Initialize all numbers as prime
    primes = []  # List to store all prime numbers found

    for i in range(2, n + 1):
        if is_prime[i]:  # If i is a prime number
            primes.append(i)
        # Mark multiples of i as non-prime, starting from i^2
        for p in primes:
            if i * p > n:
                break
            is_prime[i * p] = False
            if i % p == 0:  # Crucial step: Stop marking multiples if i is divisible by p
                break

    return primes

# Example usage
n = 10
prime_numbers = linear_sieve(n)
print("Prime numbers up to", n, ":", prime_numbers)




# def linear_sieve(n):
    
#     is_prime = [True] * (n+1)
#     primes = []
    
    
#     for i in range(2, n+1):
#         if is_prime:
#             primes.append(i)
        
#         for p in primes:
#             if i*p >n:
#                 break
            
#             is_prime[i*p] = False
            
#             if i%p ==0:
#                 break
    
#     return primes