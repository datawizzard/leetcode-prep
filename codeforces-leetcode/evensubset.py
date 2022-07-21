import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
for _ in range(int(input())):
	n=int(input())
	count=0
	arr=list(map(int,input().split()))
	for x in range(0,n):
		if arr[x]%2==0:
			ans=x+1
			count=1
	if count==1:
		print(1)
		print(ans)
	else:
		if n==1:
			print(-1)
		else:
			print(2)
			print(1,end=" ")
			print(2)

		