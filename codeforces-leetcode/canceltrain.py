import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
for _ in range(int(input())):
	n,m=map(int,input().split())
	arr=list(map(int,input().split()))
	arr1=list(map(int,input().split()))
	c=0
	for i in arr:
		if i in arr1:
			c+=1
	print(c)