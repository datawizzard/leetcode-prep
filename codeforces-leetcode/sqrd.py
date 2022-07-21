import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
for _ in range(int(input())):
	n=int(input())
	arr=list(map(int,input().split()))
	l0=0
	l2=0
	ans=0
	p2=0
	for i in range(0,n):
		arr[i]=arr[i]%4
	print(arr)
	for i in range(0,n):
		if arr[i]==0:
			ans+=i+1
			l0=i+1
		elif arr[i]==2:
			ans+=max(l0,l2)
			p2=l2
			l2=i+1
		else:
			if l0>=l2:
				ans+=i+1
			else:
				ans+=(max(l0,p2)+(i+1-l2))
	print(ans)
	