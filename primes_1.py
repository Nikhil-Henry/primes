
import time
from primes_base import is_prime
primes =[]
n = int(input('enter primes till...  '))
start_time =  time.time()
for num in range(2,n):
	if(is_prime(num)==True):
		primes.append(num)
print(primes)
print(len(primes))
print('runtime:', (time.time()-start_time))


