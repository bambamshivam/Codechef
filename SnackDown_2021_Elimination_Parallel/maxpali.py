import math;from heapq import heappush,heappop,heapify;import random;import string;from collections import deque;from bisect import bisect,bisect_left,bisect_right,insort;import sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000000+7;mod2=998244353
for _ in range(I()):
	n=I()
	if n==2:
		print('ab');continue
	def solve(i):
		c=""
		for j in range(i):
			if j%2==0:
				c+='a'
			else:
				c+='b'
		return c
	if n%2==1:
		i=0
		for i in range(2,n+1):
			if n%i==0:
				break
		c=solve(i)
		print(c*(n//i))
	else:
		s="";t=n//2
		i=0
		for i in range(2,t+1):
			if t%i==0:
				break
		c="abcdefghijklmnopqrstuvwxyz"
		while len(c)<i:
			c*=2
		c=c[:i]
		for j in range(n//i):
			if j%2==0:
				s+=c
			else:
				s+=c[::-1]
		print(s)