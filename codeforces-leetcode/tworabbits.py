import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
for _ in range(int(input())):
	x,y,a,b=map(int,input().split())
	c,d=divmod(y-x,a+b)
	print(-1 if d!=0 else c)