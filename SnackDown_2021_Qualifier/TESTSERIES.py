import math;import heapq;import string;from collections import deque;from bisect import bisect,bisect_left,bisect_right,insort;import sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());H=1000000000+7
for _ in range(I()):
	l=L()
	a=[0]*3
	for i in l:
		a[i]+=1
	if a[1]==a[2]:
		print("DRAW")
	elif a[1]>a[2]:
		print("INDIA")
	else:
		print("ENGLAND")