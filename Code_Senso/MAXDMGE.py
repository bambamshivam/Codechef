import math;from heapq import heappush,heappop,heapify;import random;import string;from collections import deque;from bisect import bisect,bisect_left,bisect_right,insort;import sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());H=1000000000+7
for _ in range(I()):
	n=I()
	a=L();l=[]
	for i in range(n):
		if i==0:
			l.append(a[i]&a[i+1])
		elif i==n-1:
			l.append(a[i]&a[i-1])
		else:
			l.append(max(a[i]&a[i-1],a[i]&a[i+1]))
	print(*l)