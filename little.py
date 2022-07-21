import sys
import math
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
for _ in range(int(input())):
	n,m=map(int,input().split())
	print(("W")+(m-1)*("B")+(n-1)*("\n"+"B"*m))