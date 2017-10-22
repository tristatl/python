import re

#email testRegularExpression
#alphabet and numbers and underline and hyphen and dot is ok
expr = re.compile(r'^[0-9a-zA-Z_\.]{1,20}@[0-9a-zA-Z_-]+(\.[0-9a-zA-Z_-]+){1,10}$')
s = 'bill.gates@gmail.com'
if expr.match(s):
	print('OK')
else:
	print('NO')
	
s2 = 'abcdefghijklmn@163.com'
if expr.match(s2):
	print('OK')
else:
	print('NO')