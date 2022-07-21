import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
for _ in range(int(input())):
	n=int(input())
	arr=list(map(int,input().split()))
	a=[]
	count=0
	for i in range(n):
		if arr[i]==1:
			a.append(i)
	print(a)
	for i in range(len(a)-1):
		while(a[i+1]-a[i]>1):
			count+=1
			a[i]+=1
	print(count)
