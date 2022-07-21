import sys
import math
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
for _ in range(int(input())):
	n=input()
	X=math.floor(int(n)**(1/17))
	print(X)