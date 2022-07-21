import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
for _ in range(int(input())):
	n=int(input())
	A=list(map(int,input().split()))
	B=list(map(int,input().split()))
	count=0
	con=0
	for i in range(n):
		if B[i]==1:
			con+=1
	for i in range(n-1):
		for j in range(i+1,n):
			if A[i]<A[j] and B[i]!=1:
				count+=1
			else:
				break
	print(count+n-con)