import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
import math
for _ in range(int(input())):
	n=int(input())
	a=list(map(int,input().split()))
	for i in a:
		# print(int(math.log(i,2)),end=" ")
		print(2**(int(math.log2(i))),end=" ")
	print()  