import sys
import math
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
for _ in range(int(input())):
	n=int(input())
	s=input()
	count=0
	for i in range(n-1):
		if s[i]==s[i+1]:
			count+=1
	print(math.ceil(count/2))
	

	

