import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
for _ in range(int(input())):
	n=int(input())
	arr=list(map(int,input().split()))
	i,j=0,n-1
	while i<=j:
		print(arr[i],end=" ")
		if i==j:
			break;
		print(arr[j],end=" ")
		i+=1
		j-=1
		# print(i,j)
	print()
