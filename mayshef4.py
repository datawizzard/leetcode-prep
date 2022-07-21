import sys
import operator
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
for _ in range(int(input())):
	X,Y,L,R=map(int,input().split())
	MAX = 32  
	ans=0
	for bit in range(MAX): 
		tempBit = 1 << bit
		bitOfX = X & Y & tempBit 
		print(bitOfX,tempBit)
		ans+= bitOfX;  
	print(ans) 
