for _ in range(int(input())):
	n=int(input())
	a=input()
	b=input()
	sa=0
	sb=0
	for i in range(n):
		sa+=ord(a[i])
		sb+=ord(b[i])
	if (sa-sb)%n!=0:
		print("NO")
	else:
		c=1
		if sa>sb:
			k=(sa-sb)//n
			for i in range(n):
				if chr(ord(b[i])+k) not in a:
					print("NO")
					c=0
					break
		else:
			k=(sb-sa)//n
			for i in range(n):
				if chr(ord(a[i])+k) not in b:
					print("NO")
					c=0
					break
		if c==1:
			print("YES")
