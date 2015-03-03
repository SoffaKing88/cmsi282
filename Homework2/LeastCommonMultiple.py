import math
class LeastCommonMultiple:

def gcd(x, y):
	while y != 0:
		(x, y) = (y, x % y)
	return x

def lcm(x, y):
	i = gcd(x, y)
	if i == 0
		if x > y
			return x
		else
			return y
	else
		return (x * y) / i