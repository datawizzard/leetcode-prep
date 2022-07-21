import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
for _ in range(int(input())):
	n=int(input())
	arr=list(map(int,input().split()))
	arr.sort(reverse=True)
	profit=0
	x=0
	for i in range(0,n):
		if arr[i]>0:
			profit=profit+arr[i]
			profit=profit-i
			if x-profit>=0:
				break
			x=profit
	print(x%(10**9+7))
