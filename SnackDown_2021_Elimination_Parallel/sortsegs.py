import math;from heapq import heappush,heappop,heapify;import random;import string;from collections import deque;from bisect import bisect,bisect_left,bisect_right,insort;import sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000000+7;mod2=998244353
for _ in range(I()):
	n,k=M()
	a=L();f=0
	for i in range(n):
		if a[i]!=i+1:
			f=1;break
	if f==0:
		print(0);continue
	i=0;j=n-1
	while i<n:
		if a[i]!=i+1:
			break
		i+=1
	while j>=0:
		if a[j]!=j+1:
			break
		j-=1
	if j-i+1<=k:
		print(1);continue
	b=a[:]
	a=sorted(a[:min(i+k,n)])+a[min(i+k,n):]
	a=a[:max(j-k+1,0)]+sorted(a[max(0,j-k+1):])
	b=b[:max(j-k+1,0)]+sorted(b[max(0,j-k+1):])
	b=sorted(b[:min(i+k,n)])+b[min(i+k,n):]
	f1=f2=0
	for i in range(n):
		if a[i]!=i+1:
			f1=1
		if b[i]!=i+1:
			f2=1
	if f1==0 or f2==0:
		print(2);continue
	else:
		print(3)