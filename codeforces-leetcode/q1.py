import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
for _ in range(int(input())):
	n=int(input())
	arr=list(map(int,input().split()))
	a=[0]*(n-1)
	count=0
	count1=0
	for i in range(n-1):
		a[i]=arr[i+1]-arr[i]
	for i in range(n-1):
		if a[i]>0:
			count+=1
		else:
			count1+=1
	print(count)
	print(count1)
	if count>=(n-1)/2 and count1>=(n-1)/2:
		print(arr)
	else:
		if count<=(n-1)/2:
			for i in range(n-1):
				if arr[i+1]-arr[i]<0:
					arr[i+1]=(-arr[i+1])
		print(arr)
		

