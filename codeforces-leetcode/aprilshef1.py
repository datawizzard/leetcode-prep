import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
for _ in range(int(input())):
	n=int(input())
	arr=list(map(int,input().split()))
	j=0
	flag=0
	count1=0
	for i in range(0,n):
		if arr[i]==1:
			count1+=1
			if i-j>=6 or count1==1:
				flag=1
			else:
				flag=0
				break
			j=i
	if flag==1:
		print("YES")
	else:
		print("NO")