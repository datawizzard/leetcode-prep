import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
for _ in range(int(input())):
	n=int(input())
	arr=list(map(int,input().split()))
	ar=[]
	for i in range(n):
		if arr[i]==1:
			ar.append(i)
	print(ar)
	if len(ar)==1:
		print("YES")
	else:
		for j in range(len(ar)-1):
			if ar[j+1]-ar[j]<6:
				print("NO")
				break;
			elif j==n-1:
				print("YES")
