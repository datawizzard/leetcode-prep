import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
for _ in range(int(input())):
	n=int(input())
	arr=list(map(int,input().split()))
	b=[0]*(n-1)
	d=[0]*(n-1)
	ans=1
	l=0
	flag=0
	for i in range(n-1):
		b[i]=arr[i+1]-arr[i]
	if all(x <=2 for x in b):
		flag=1
	else:
		for i in range(n-1):
			if b[i]<=2:
				ans+=1
			else:
				d[l]=ans
				l+=1
				ans=1
	max1=d[0]
	min1=d[0]
	if flag==1:
		print(n,n)
	else:
		for i in range(l):
			if d[i]<min1:
				min1=d[i]
			if d[i]>max1:
				max1=d[i]
		print(min(min1,ans),max(max1,ans))
		

	

	

