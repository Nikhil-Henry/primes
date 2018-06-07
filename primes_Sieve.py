from primes_base import is_prime

x = int(input('Enter the range'))
non_primes = []
primes = []
product_of_primes = 1

for j in range(2,x):
	if(is_prime(j)==True):
		primes.append(j)
	else:
		non_primes.append(j)
for n in primes:
	product_of_primes = product_of_primes*n
print(product_of_primes+1)