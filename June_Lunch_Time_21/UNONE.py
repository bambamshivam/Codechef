import math
def S():
	return input()
def M():
	return map(int,input().split())
def I():
	return int(S())
def L():
	return list(M())

for _ in range(I()):
	n=I()
	l=L()
	e0=[]
	e1=[]
	for i in l:
		s=bin(i)
		if s[-1]=='0':
			e0.append(i)
		else:
			e1.append(i)
	a=e0+e1
	print(*a)
