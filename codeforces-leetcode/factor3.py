import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
for _ in range(int(input())):
	n=int(input())
	arr=list(map(int,input().split()))
	x0,x1,x2=0,0,0
	for i in range(n):
		if arr[i]%3==0:
			x0+=1
		elif arr[i]%3==1:
			x1+=1
		else:
			x2+=1
	if ((x0 == 0 and x1 != 0 and x2 != 0) or x0 > x1 + x2 + 1):
		print("No")
	else:
		print("Yes")
