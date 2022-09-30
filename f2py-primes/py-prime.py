import primes


sieve_array = primes.sieve(100)
prime_numbers = primes.logical_to_integer(sieve_array, sum(sieve_array))

print(prime_numbers)

