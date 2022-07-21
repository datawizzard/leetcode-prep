import math
import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
for _ in range(int(input())):
	x,k=map(int,input().split())
	c=0
	while x%2==0:
		c+=1
		x=x/2
	for  i in range(3,int(math.sqrt(x))+1,2):
		while x%i==0:
			c+=1
			x=x/i
	if x>2:
		c+=1
	if c>=k:
		print(1)
	else:
		print(0)