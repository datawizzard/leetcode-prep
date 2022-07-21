import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
for _ in range(int(input())):
	n,s=map(int,input().split())
	arrp=list(map(int,input().split()))
	arr1=list(map(int,input().split()))
	sum1=100-s
	flag=0
	for i in range(0,n):
		for j in range(i+1,n):
			if arr1[i]!=arr1[j]:
				x=arrp[i]+arrp[j]
				if x<=sum1:
					flag=1
					break;
	if flag==1:
		print("yes")
	else:
		print("no")
