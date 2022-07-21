import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
for _ in range(int(input())):
	n,x=map(int,input().split())
	arr=list(map(int,input().split()))
	l=[i%2 for i in arr]
	print(l)
	c=l.count(1)
	if(c==0 or (c==n and x%2==0) or (c%2==0 and n==x)):
		print("No")
	else:
		print("Yes")

