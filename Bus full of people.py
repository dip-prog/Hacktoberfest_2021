for i in range(int(input())):
	n,m,q=map(int, input().split())
	c=0
	flag=0
	l=[]
	for i in range(q):
		a,b=map(str,input().split())
		if a=="+":
			c+=1
			r=int(b)
			if i==0:
				l.append(r)
			elif r in l:
				flag=1
			elif r not in l:
				l.append(r)
			if (c>m):
				flag=1
		elif a=="-":
			c=c-1
			r=int(b)
			if (c<0 or r not in l):
				flag=1
			if r in l:
				l.remove(r)
	if flag==1:
		print("Inconsistent")
	else:
		print("Consistent")# cook your dish here
