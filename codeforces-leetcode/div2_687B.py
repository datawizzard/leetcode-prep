import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
import math
for _ in range(int(input())):
	n,k=map(int,input().split())
	arr=list(map(int,input().split()))
	m=n
	l=set(arr)
	for i in l:
		j,s=0,0
		while(j<n):
			if arr[j]!=i:
				s+=1
				j+=k
			else:
				j+=1
		m=min(m,s)
	print(m)


