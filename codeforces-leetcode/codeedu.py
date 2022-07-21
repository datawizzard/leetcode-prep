import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
for _ in range(int(input())):
	n=int(input())
	arr=[]
	arr1=[]
	for i in range(n):
		p,q=map(int,input().split())
		arr.append(p)
		arr1.append(q)
	for i in range(0,len(arr)-1):
		if arr[i+1]>arr[i] and arr1[i+1]>=arr1[i]:
			flag=1
		else:
			flag=0
			break;
	if flag==1:
		print("YES")
	else:
		print("NO")
	
