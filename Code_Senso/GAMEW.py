import math;from heapq import heappush,heappop,heapify;import random;import string;from collections import deque;from bisect import bisect,bisect_left,bisect_right,insort;import sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());H=1000000000+7
for _ in range(I()):
	n=I()
	s=S()
	i=c=0
	while i<n:
		j=i+1
		while j<n and s[i]==s[j]:
			j+=1
		c+=1
		i=j
	if (c-2)%3==0:
		print("RAMADHIR")
	else:
		print("SAHID")