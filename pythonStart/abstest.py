import math

def quadratic(a,b,c):
	tmp = b*b-4*a*c
	if tmp < 0:
		return 
	elif tmp == 0:
		return -b/2*a
	else:
		return (-b+sqrt(tmp))/2*a
		