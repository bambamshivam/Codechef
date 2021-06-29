import math
def S():
	return input()
def M():
	return map(int,input().split())
def I():
	return int(input())
def L():
	return list(map(int,input().split()))

for _ in range(I()):
	n,m,k=M()
	ar=[[0 for i in range(m)] for j in range(n)]
	for i in range(n*m):
		a,b=M()
		if i%2==0:
			ar[a-1][b-1]=("A",i)
		else:
			ar[a-1][b-1]=("B",i)
		for j in range(n-k):
			for t in range(m-k):
				f=0
				ans=""
				for p in range(j,j+k):
					for q in range(t,t+k):
						if ar[p][q]!=ar[j][t]:
							f=1
							break
					if f==1:
						break
				if f==0:
					if ar[j][t]=='A':
						ans="Alice"
					else:
						ans="Bob"
					break
			if f==0:
				break
		if f==0:
			break
	if f==0:
		for j in range(n*m-i -1):
			a,b=M()
		print(ans)






