import math;from heapq import heappush,heappop,heapify;import random;import string;from collections import deque;from bisect import bisect,bisect_left,bisect_right,insort;import sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());H=1000000000+7
for _ in range(I()):
	n,k=M()
	l=[];p=[]
	for i in range(n):
		a=L()
		l.append(a)
		p+=a
	p.sort()
	print(p[-math.ceil((n+1)//2)*n])