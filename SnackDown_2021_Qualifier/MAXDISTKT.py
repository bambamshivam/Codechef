import math;import heapq;import string;from collections import deque;from bisect import bisect,bisect_left,bisect_right,insort;import sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());H=1000000000+7
for _ in range(I()):
	n=I()
	l=L()
	b=sorted(list(enumerate(l)),key=lambda x:x[1])
	t=0
	a=[];c=[]
	for i in range(n):
		if t<b[i][1]:
			a.append(b[i][1]+t)
			t+=1
		else:
			a.append(b[i][1])
	d=[0]*n
	for i in range(n):
		d[b[i][0]]=a[i]
	for i in range(n):
		c.append(d[i]%l[i])
	print(*d)