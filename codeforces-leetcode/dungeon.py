import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
import math
for _ in range(int(input())):
	a,b,c=map(int,input().split())
	p=min(a,b,c)
	s=a+b+c
	if s%9==0 and p>=s//9:
		print("YES")
	else:
		print("NO")
