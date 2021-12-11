import math;import sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
for _ in range(I()):
	s=list(S());n=len(s);ans=0
	if s[-1]=='N':s[-1]='P';ans+=1
	for i in range(n-1):
		if s[i]=='N' and s[i+1]!='P':
			ans+=1
			s[i+1]='P'
	c1=s.count('N')
	print(ans+abs(c1-n//3))