import math
def iss(n):
	s=0
	if n==0 or n==1:
		s=1
	else:
		di={}
		while n%2==0:
			if 2 in di:
				di[2]+=1
			else:
				di[2]=1
			n=n//2
		for i in range(3,int(math.sqrt(n))+1,2):
			while n%i==0:
				n=n//i
				if i in di:
					di[i]+=1
				else:
					di[i]=1
		if n>2:
			if n in di:
				di[n]+=1
			else:
				di[n]=1
		for ke in di:
			if di[ke]==1:
				s+=nl(ke)
			else:
				s+=(nl(ke)+nl(di[ke]))
	return s


def nl(n):
	c=0
	while n>0:
		n=n//10
		c+=1
	return c

def minsub(l,s):
	n=len(l)
	dp=[[True for i in range(s+1)] for i in range(n+1)]
	for i in range(n+1):
		for j in range(s+1):
			if i==0:
				dp[i][j]=(False,0)

	for i in range(n+1):
		for j in range(s+1):
			if j==0:
				dp[i][j]=(True,0)

	for i in range(1,n+1):
		for j in range(1,s+1):
			if l[i-1]>j:
				dp[i][j]=dp[i-1][j]
			else:
				p=dp[i][j-l[i-1]]
				q=dp[i-1][j]
				if p[0]==True:
					if q[0]==True:
						dp[i][j]=(True,min(dp[i][j-l[i-1]][1]+1,dp[i-1][j][1]))
					else:
						dp[i][j]=(True,dp[i][j-l[i-1]][1]+1)
				else:
					if q[0]==True:
						dp[i][j]=(True,dp[i-1][j][1])
					else:
						dp[i][j]=(False,0)

	return dp[n][s][1]

l=[]
for i in range(1,2*(10**5) + 1):
	if iss(i)==nl(i):
		l.append(i)


for _ in range(int(input())):
	a,b=map(int,input().split())
	i=0
	while i<len(l):
		if l[i]>(b-a):
			break
		i+=1
	print(minsub(l[:i],(b-a)))





