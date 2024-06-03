numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

primes = []
not_primes = []

for i in range(2, 16):
    k = 0
    for j in range(2, i // 2 + 1):

        if (i % j == 0):
            k = k + 1
    if (k <= 0):
        primes.append(i)

    else:
        not_primes.append(i)

print('Primes :', primes)
print('Not_primes :', not_primes)
