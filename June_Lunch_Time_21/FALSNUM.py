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
	s=S()
	if len(s)==1:
		if s[0]=='1':
			print(10)
		else:
			print('1'+s[0])
	else:
		if s[0]=='1':
			print(s[0]+'0'+s[1:])
		else:
			print('1'+s)