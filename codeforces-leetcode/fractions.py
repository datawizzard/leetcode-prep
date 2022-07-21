import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
import math
n=int(input())
count=0
for i in range(1,n):
	for j in range(i+1,n+1):
		p=i*(j+1)
		q=(i+1)*j
		x=math.gcd(p,q)
		l=p//x
		m=q//x
		if l+1==m:
			#print(i,j)
			count+=1
print(count)

