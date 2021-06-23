import math
def fa(n):
	di={}
	for i in range(1,n//2 + 1):
		if n % i== 0:
			di[i]=1
	di[n]=1
	return di

def cald(s,j,ke,c1):
	c=0
	n=len(s)
	c0=n-c1
	for i in range(j,n,ke):
		if s[i]!='1':
			c+=1
	c0-=c
	c+=((ke-1)*(n//ke) -c0)
	return c


for _ in range(int(input())):
	n=int(input())
	s=input()
	c1=0
	for ch in s:
		if ch=="1":
			c1+=1
	di=fa(n)
	m=10**10
	for ke in di:
		j=0
		while j<ke:
			t=cald(s,j,ke,c1)
			if t<m:
				m=t
			j+=1
	print(m)





	
		
