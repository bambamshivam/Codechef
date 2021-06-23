import math
x,y=map(int,input().split())
n,k=map(int,input().split())
di={}
for i in range(n):
	x1,y1,t=input().split()
	x1=int(x1)
	y1=int(y1)
	di[(x1,y1,t)]=math.sqrt((x-x1)**2 + (y-y1)**2)
c,s,o=0,0,0
for it in sorted(di.items(), key=lambda x:x[1]):
	if c==k:
		break
	if it[0][2]=='S':
		s+=1
	else:
		o+=1
	c+=1
if s<=o:
	print("EASY AS CAKE")
else:
	print("IT IS EXHILARATING")
