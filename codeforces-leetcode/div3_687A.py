import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
import math
for _ in range(int(input())):
	n=int(input())
	ans=0
	x=str(n)
	y=len(x)
	if y==1:
		ans=1
	elif y==2:
		ans=3
	elif y==3:
		ans=6
	elif y==4:
		ans=10
	l=(int(x[0])-1)*10
	print(ans+l)
