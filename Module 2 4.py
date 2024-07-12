numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for a in range(1, len(numbers) + 1):
    count = 0
    for b in range(1, a + 1):
        if a % b == 0:
            count +=1
    if count == 2:
        primes.append(a)
    if count !=2 and a != 1:
        not_primes.append(a)
print('Primes:', primes)
print('Not Primes:', not_primes)
