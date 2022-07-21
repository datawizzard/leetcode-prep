import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
for _ in range(int(input())):
	x,y,n=map(int,input().split())
	count=0
	for i in range(0,n+1):
		if x^i<y^i:
			print(i,end=" ")
			count+=1
	print(count)