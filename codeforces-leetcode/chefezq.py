import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
for _ in range(int(input())):
	n,k=map(int,input().split())
	arr=list(map(int,input().split()))
	flag=0
	ans=0
	for i in range(n-1):
		if arr[i]<k:
			ans=i
			flag=1
			break
		arr[i+1]+=arr[i]-k
	if flag==1:
		print(ans)
	else:
		ans=n+arr[-1]//k
		print(ans)

