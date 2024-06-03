numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

primes = []
not_primes = []

for i in range(2, 15):
    is_prime = 0
    for j in range(2, numbers[i] // 2 + 1):

        if (numbers[i] % j == 0):
            is_prime = is_prime + 1
    if (is_prime <= 0):
        primes.append(numbers[i])

    else:
        not_primes.append(numbers[i])

print('Primes :', primes)
print('Not_primes :', not_primes)
