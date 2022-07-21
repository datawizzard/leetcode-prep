import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
for _ in range(int(input())):
	n=int(input())
	arr=list(map(int,input().split()))
	arr.sort(reverse=True)
	x=[]
	y=[]
	if n==1:
		print(*arr)
	else:
		x.append(arr[0])
		y.append(arr[1])
		for i in range(2,n):
			if sum(x)>=sum(y):
				y.append(arr[i])
			else:
				x.append(arr[i])
		print(max(sum(x),sum(y)))
