import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
for _ in range(int(input())):
	n,k=map(int,input().split())
	arr=list(map(int,input().split()))
	min1=99999999
	flag=0
	for i in arr:
		if k%i==0:
			rem=k//i
			if min1>rem:
				min1=rem
				pos=i
				flag=1
	if flag==1:
		print(pos)
	else:
		print(-1) 