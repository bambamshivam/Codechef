import math;from heapq import heappush,heappop,heapify;import random;import string;from collections import deque;from bisect import bisect,bisect_left,bisect_right,insort;import sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());H=1000000000+7
for _ in range(I()):
	n,v=M()
	if v>=n-1:
		print((n-1)*n//2,n-1);continue
	print((n-1)*n//2,v-1+(n-v)*(n-v+1)//2)