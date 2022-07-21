import sys
from itertools import combinations_with_replacement
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
n=int(input())
z=[]
count=0
def prim(num):
	if num > 1:
		for i in range(2,num):
			if (num % i==0):
				break
			else:
				return 1
	else:
		return 0
for i in range(n+1):
	z.append(i)
	c=list(combinations_with_replacement(z,2))
print(c)
for i in range(len(c)):
	l=(c[i][0]+c[i][1])
	if(prim(l)==1 and c[i][0]<=n and c[i][1]<=n):
		count=count+1
print(count)