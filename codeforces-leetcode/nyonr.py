import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
for _ in range(int(input())):
	n=int(input())
	c=0
	arr=list(map(int,input().split()))
	for i in range(n):
		if arr[i]==0:
			c+=1
	if c%2==0:
		print("NO")
	else:
		for i in range(n):
			if arr[i]
