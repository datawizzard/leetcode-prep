import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
for _ in range(int(input())):
	n,k=map(int,input().split())
	arr=list(map(int,input().split()))
	count=0
	sum1=0
	c=1
	if any(i>k for i in arr):
		print(-1)
	else:
		for i in arr:
			sum1+=i
			if sum1<=k:
				count=c
			else:
				sum1=i
				count+=1
				c=count
		print(count)