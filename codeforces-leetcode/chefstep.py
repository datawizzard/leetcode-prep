import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
for _ in range(int(input())):
	n,k=map(int,input().split())
	arr=list(map(int,input().split()))
	arr1=[]
	for i in range(n):
		if arr[i]%k==0:
			arr1.append(1)
		else:
			arr1.append(0)
	print(''.join(map(str,arr1)))