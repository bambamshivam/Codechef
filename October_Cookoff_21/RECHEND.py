import math;from heapq import heappush,heappop,heapify;import random;import string;from collections import deque;from bisect import bisect,bisect_left,bisect_right,insort;import sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());H=1000000000+7
for _ in range(I()):
	n=I();d={};p=[]
	for i in range(n):
		a,b=M()
		d[(a,b)]=1
		p.append((a,b))
	p.sort(key=lambda x:x[1])
	f1=f2=1
	i,j=p[0][0],p[0][1];t=0
	while t<n and 1<=j<=n and 1<=i<=n:
		if p[t][0]!=i or p[t][1]!=j:
			f1=0
			break
		else:
			t+=1
		i-=1;j+=1
	i,j=p[-1][0],p[-1][1];t=n-1
	while t>=0 and 1<=j<=n and 1<=i<=n:
		if p[t][0]!=i or p[t][1]!=j:
			f2=0
			break
		else:
			t-=1
		i+=1;j-=1
	if f1==f2==0:
		print("YES")
	else:
		print("NO")