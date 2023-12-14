# Write a Python program to generate prime numbers between 1 to n, where n is provided as input by
# the user.

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def generate_primes(n):
    primes = [num for num in range(2, n+1) if is_prime(num)]
    return primes

n = int(input("Enter a value of n: "))

if n < 0:
    print("Please enter a non-negative number.")
else:
    prime_numbers = generate_primes(n)
    print(f"Prime numbers between 1 and {n}: {prime_numbers}")
