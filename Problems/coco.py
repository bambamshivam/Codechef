import math
for _ in range(int(input())):
	xa,xb,Xa,Xb=map(int,input().split())
	print(int(math.ceil(Xa/xa))+int(math.ceil(Xb/xb)))