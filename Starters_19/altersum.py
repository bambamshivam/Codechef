import math;import sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
for _ in range(I()):
	n=I()
	a=L();dp=[0]*(n+1)
	for i in range(n):
		if i%2==0:
			dp[i+1]+=a[i]+dp[i]
		else:
			dp[i+1]+=-a[i]+dp[i]
	m=dp[-1]
	for i in range(n):
		s1=dp[i];s2=dp[-1]-dp[i+1]
		if i%2==1:
			if (n-i-1)%2==0:
				m=max(m,s1-s2-a[i])
			else:
				m=max(m,s1-s2+a[i])
		else:
			if (n-i-1)%2==0:
				m=max(m,s1-s2+a[i])
			else:
				m=max(m,s1-s2-a[i])
	print(m)