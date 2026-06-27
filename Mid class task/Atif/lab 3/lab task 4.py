def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

total = 0

for num in range(1000):
    if is_prime(num):
        total += num

print("Sum of primes below 1000:", total)