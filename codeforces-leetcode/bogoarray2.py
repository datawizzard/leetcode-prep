import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
for _ in range(int(input())):
	n=int(input())
	arr=list(map(int,input().split()))
	arr.sort(reverse=True)
	for i in range(0,n):
		print(arr[i],end=" ")
	print()