import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
for _ in range(int(input())):
	n=int(input())
	a=list(map(int,input().split()))
	for i in range(0,n):
		for j in range(i,n):
			if j-a[j]==i-a[i]:
				temp=a[j]
				a[j]=a[i]
				a[i]=temp
	for i in range(0,n):
		print(a[i],end=" ")
	print()