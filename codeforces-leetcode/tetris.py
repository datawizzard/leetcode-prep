import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
for _ in range(int(input())):
	n=int(input())
	arr=list(map(int,input().split()))
	count=0
	ind=0
	for i in arr:
		if i%2==0:
			count+=1
		if i%2==1:
			ind+=1
	if count==n or ind==n:
		print("YES")
	else:
		print("NO")