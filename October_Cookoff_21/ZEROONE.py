import math;from heapq import heappush,heappop,heapify;import random;import string;from collections import deque;from bisect import bisect,bisect_left,bisect_right,insort;import sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());H=1000000000+7
for _ in range(I()):
	n=I()
	l=L();a=[];b=[]
	for i in range(n):
		if i%2==0:
			a.append(l[i])
		else:
			b.append(l[i])
	a.sort(reverse=True);b.sort()
	for i in range(len(a)):
		l[2*i]=a[i]
	for i in range(len(b)):
		l[2*i+1]=b[i]
	s=sum(l)-sum(a)
	print(*l);ans=0
	for i in range(n):
		if i%2==0:
			ans+=(s*l[i])
		else:
			s-=l[i]
	print(ans)