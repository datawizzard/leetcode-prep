import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
from collections import defaultdict
from collections import OrderedDict
for _ in range(int(input())):
	f = defaultdict(list)
	n = int(input())
	a = list(map(int,input().split()))
	c = list(map(int,input().split()))
	ans = 0
	p = 0
	for i in range(n):
	    f[c[i]].append(a[i])
	f1 = OrderedDict(sorted(f.items()))
	for i in f1:
		total=sum(f1[i])
		if p + total< n:
		    ans += i*total
		    p += total
		else:
		    req = n-p
		    ans += req*i
		    p += req
		if p == n:
		    break
	print(ans)