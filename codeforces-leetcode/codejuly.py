import sys
import math
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
for _ in range(int(input())):
	n=int(input())
	arr=list(map(int,input().split()))
	count=0
	for i in range(n-1):
		count+=abs(arr[i+1]-arr[i])-1
	print(count)