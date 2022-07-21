import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
for _ in range(int(input())):
	n=int(input())
	sum1=0
	arr=list(map(int,input().split()))
	for i in range(n):
		if arr[i]==0:
			sum1+=1
		else:
			sum1+=arr[i]
	if sum1%n==0:
		print("YES")
	else:
		print("NO")