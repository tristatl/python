# from __future__ import division
#-*- coding: utf-8 -*-
'''
print "Please enter you name:"
name = raw_input()
print name

a = 12
b = a
print a
print b
a = 13
print a
print b

print("中文")
print(ord('A'))
print(chr(66))

name = b"Ivy"
print(len(name))
new = "中国".encode('utf-8')
print(new)
print("中文")


PI = 3.1415926
s1 = 72
s2 = 85
r = "Ivy"
print('%s' % r)
print('%.2f' % PI)
print('Hello, %d %d' % (s1,s2))


L = (['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa'])
print(L[0][0])
print(L[1][1])
print(L[2][2])
L[0].append('IVY')
print(L[0])
L[1].pop()
print(L[1])
L[2].pop(0)
print(L[2])


ages = input()
age = int(ages)

if age >= 18:
	print('you')
	print('are')
	print('an','adult')
elif age > 6:
	print('you are a teenager')
else:
	print('child')
	
# c++ 的 atoi()函数强制 str[]类型转换成int
# python没有强制字符串类型的转换...吧？？

a = '13'
b = int(a)
print(a)
print(b)

'''

sum = 0
num = list(range(101))
for i in num:
	sum += i
	if sum > 2000: 
		break
print(sum)