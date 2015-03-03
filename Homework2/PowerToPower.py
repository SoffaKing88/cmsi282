import math

class PowerToPower:

	a = 3
	b = 3
	c = 3
	
	i = 2
	exponent = b
	while i <= c:
		b = exponent*b
		i+=1
	
	i = 2

	result = a
	while i <= b:
		result = result*a
		i+=1

	print(result)