import math;import sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
from collections import defaultdict
for _ in range(I()):
	n=I()
	a=L();ans=0
	freq=[0]*(1<<20);F=[0]*(1<<20)
	for i in a:freq[i]+=1
	for i in range(20):
		for mask in range(1<<20):
			if i==0:
				F[mask]=freq[mask]
			if mask&(1<<i):
				F[mask]+=F[mask^(1<<i)]
	for i in a:
		ans+=(F[i]-1)*(n-2)
	print(ans)