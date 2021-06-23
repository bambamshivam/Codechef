for _ in range(int(input())):
	x1,x2,x3,r=map(int,input().split())
	lt=(x3-r,x3+r)
	rt=(x1,x2)
	if x1>x2:
		rt=(x2,x1)
	if lt[1]<=rt[0] or lt[0]>=rt[1]:
		print(rt[1]-rt[0])
	elif lt[0]<=rt[0] and lt[1]>=rt[0] and lt[1]<=rt[1]:
		print(rt[1]-lt[1])
	elif lt[0]>=rt[0] and lt[0]<=rt[1] and lt[1]>=rt[1]:
		print(lt[0]-rt[0])
	elif lt[0]>=rt[0] and lt[1]<=rt[1]:
		print((rt[1]-lt[1])+(lt[0]-rt[0]))
	else:
		print(0)