import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
for _ in range(int(input())):
	n,q=map(int,input().split())
	arr=list(map(int,input().split()))
	for _ in range(q):
		x,y=map(int,input().split())
		for i in range(n):
			if i==x-1:
				arr[i]=y
				break;
		count=1
		temp=1
		for i in range(1,n):
			if arr[i-1]!=arr[i]:
				count+=1
			else:
				temp=count
				c

		print(arr)
		print(count)