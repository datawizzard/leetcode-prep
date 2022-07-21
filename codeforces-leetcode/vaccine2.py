import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
import math
for _ in range(int(input())):
	n,d=map(int,input().split())
	ages=list(map(int,input().split()))
	count=0
	for i in range(n):
		if ages[i]>=80 or ages[i]<=9:
			count+=1
	print(math.ceil(count/d)+math.ceil((n-count)/d))

