import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
for _ in range(int(input())):
	a=input()
	b=input()
	c=0
	if a==b:
		print(0)
	else:
		n=len(a)
		l=[0]*n
		for i in range(n):
			if a[i]!=b[i]:
				l[i]=1
		for i in range(n):
			if l[i]==0:
				continue;
			r=i
			while r<n and l[r]==1:
				l[r]=0
				r+=2
			c+=1
		print(c)
		