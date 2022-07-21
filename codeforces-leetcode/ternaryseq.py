import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
for _ in range(int(input())):
	n=int(input())
	arr=list(map(int,input().split()))
	m=min(arr)
	k=0
	flag=0
	x=[]
	y=[]
	for i in range(n):
		if arr[i]%m==0:
			x.append(i)
			y.append(arr[i])
			k+=1
	y.sort()
	for i in range(k):
		arr[x[i]]=y[i]
	print(arr)
	for i in range(n-1):
		if arr[i]>arr[i+1]:
			flag=1
	if flag==1:
		print("NO")
	else:
		print("YES")



