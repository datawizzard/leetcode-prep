import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
for _ in range(int(input())):
	count=0
	n=int(input())
	arr=list(map(int,input().split()))
	arr.sort()
	for i in range(1,n):
		if arr[i-1]==arr[i]:
			count+=1
	print(n-count)
