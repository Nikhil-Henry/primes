import math 
def is_prime(num):
	if(num==2):
		return True
	if(num>2 and num%2==0):
		return False
	max_divisor = math.floor(math.sqrt(num))
	if(num==0 or num==1):
		return False
	for d in range(2,max_divisor+1):
		if(num%d==0):
			return False
	return True

#number = int(input('Enter a number'))
#print(is_prime(number))