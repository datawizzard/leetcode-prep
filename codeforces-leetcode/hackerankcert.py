import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
for _ in range(int(input())):
	n=int(input())
	arr=list(map(int,input().split()))
	ans=0
	for i in range(len(arr)):
		if arr[i]%2==0:
			ans+=arr[i]//2
		else:
			ans+=arr[i]//2
			if i!=len(arr)-1 and arr[i+1]!=0:
				arr[i+1]+=1
	print(ans)
	

