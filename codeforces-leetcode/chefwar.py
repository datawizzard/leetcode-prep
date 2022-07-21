import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
for _ in range(int(input())):
	x,y=map(int,input().split())
	while x>=0:
		x=x-y
		y=y//2
		print(x,y)
		if x<=0:
			print(1)
			break
		if y==0:
			print(0)
			break
