import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
for _ in range(int(input())):
	n=int(input())
	arr=list(map(int,input().split()))
	if arr[0]+arr[1]>arr[n-1]:
		print(-1)
	else:
		print(1,2,n)