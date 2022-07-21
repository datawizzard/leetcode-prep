import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
for _ in range(int(input())):
	n=int(input())
	arr=list(map(int,input().split()))
	flag=0
	x=max(arr)
	for i in range(n):
		if i==0:
			if arr[i]==x and arr[i]>arr[i+1]:
				print(i+1)
				flag=1
				break;
		elif i==n-1:
			if arr[i]==x and arr[i]>arr[i-1]:
				print(i+1)
				flag=1
				break;
		elif arr[i]==x and (arr[i]>arr[i+1] or arr[i]>arr[i-1]):
				print(i+1)
				flag=1
				break;
	if flag==0:
		print(-1)




