import math
def S():
	return input()
def M():
	return map(int,input().split())
def I():
	return int(input())
def L():
	return list(map(int,input().split()))
l={}
c=2
while c<=1000000000000000000:
	l[c]=True
	c*=2
for _ in range(I()):
	a,b=input().split()
	t=l.get(b,False)
	if t:
		print("Yes")
	else:
		print("No")