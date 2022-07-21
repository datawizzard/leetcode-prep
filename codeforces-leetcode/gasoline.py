import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
import os
from collections import defaultdict
from collections import OrderedDict
def gasoline(n,a,c):
	d = defaultdict(list)
	sol,r,total = 0,0,0
	for i in range(n):
	    d[c[i]].append(a[i])
	print(d)
	m = OrderedDict(sorted(d.items()))
	print(m)
	x=0
	for i in m:
		total=sum(m[i])
		print(total,i)
		if x+ total <= n:
		    sol += i*total
		    x=x+total
		else:
		    r = n-x
		    sol=sol+r*i
		    x =x+ r
		if x == n:
		    break
	return sol
for _ in range(int(input())):
	n = int(input())
	a = list(map(int,input().split()))
	c = list(map(int,input().split()))
	print(gasoline(n,a,c))
	
