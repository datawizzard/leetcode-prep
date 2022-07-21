import operator
from collections import defaultdict
import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
n=int(input())
arr=list(map(int,input().split()))
s = sorted(set(arr), reverse = True)
print(s)
dct = dict.fromkeys(s, 0)
print(dct)
for i in arr:
    dct[i] += 1
print(dct)
dct_n = defaultdict(list)
for k, v in dct.items():
    dct_n[v].append(k)
print(dct_n)
dct_n = sorted(dct_n.items(), key=operator.itemgetter(0), reverse = True)
print(dct_n)
for i in range(len(dct_n)):
    l =sorted(dct_n[i][1], reverse = True)
    for i in l:
        print(i, end = ' ')