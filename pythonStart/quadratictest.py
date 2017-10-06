import math

def quadratic(a,b,c):
	tmp = b*b-4*a*c
	#print(tmp)
	if tmp < 0:
		return 
	elif tmp == 0:
		return -b/(2*a)
	else:
		#print((-b+math.sqrt(tmp))/(2*a))
		#print((-b-math.sqrt(tmp))/(2*a))
		return (-b+math.sqrt(tmp))/(2*a) ,(-b-math.sqrt(tmp))/(2*a)
		