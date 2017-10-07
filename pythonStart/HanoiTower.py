def Hanoi(n,a,b,c):
	if n == 1:
		print('move',a,'-->',c)
	else:
		Hanoi(n-1,a,c,b)
		Hanoi(1,a,b,c)
		Hanoi(n-1,b,a,c)
Hanoi(3,'A','B','C')
	
	