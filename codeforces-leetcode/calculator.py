import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
for _ in range(int(input())):
	n=int(input())
	arr=list(map(int,input().split()))
	sum1=arr[0]
	for i in range(1,n):
		if sum1>=i:
			sum1+=arr[i]
	print(sum1)