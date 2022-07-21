import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
for _ in range(int(input())):
	n=int(input())
	#p=0
	arr=[]
	if n==1:
		print(n)
	else:
		print(n//2)
	for i in range(1,4):
		if i<=n:
			arr.append(i)
	if i==3 or n<3:
		print(len(arr),end=" ")
		for i in arr:
			print(i,end=" ")
	print()
	for i in range(4,n+1,2):
		if i<n:
			print(2,i,i+1)
		else:
			print(1,i)