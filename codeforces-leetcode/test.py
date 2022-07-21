import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
from itertools import groupby
arr=list(map(int,input().split()))
d = {'even':[], 'odd':[]}
mynum = [int(x) for x in arr]
print(mynum)
for k,g in groupby(mynum, lambda x: x % 2):
        if k:
            d['odd'].extend(g)
        else:
            d['even'].extend(g)
print(d)