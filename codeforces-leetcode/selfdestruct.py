import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
import sys
import math
import bisect
from sys import stdin, stdout
from math import gcd, floor, sqrt, log, ceil
from collections import defaultdict as dd
from collections import Counter as cc
from bisect import bisect_left as bl
from bisect import bisect_right as br
import functools
 
sys.setrecursionlimit(100000000)
t= lambda : int(input())
intinp = lambda: int(input().strip())
stripinp = lambda: input().strip()
fltarr = lambda: list(map(float,input().strip().split()))
arr = lambda: list(map(int,input().strip().split()))
# loop(i,n,1) = lambda : for i in range(t()):

for _ in range(int(input())):
	s=input()
	count0,count1,ans=0,0,0
	for i in s:
		if i=='0':
			count0+=1
		else:
			count1+=1
	if count0==count1:
		print(0)
	elif abs(count0-count1)%2==0 and count0*count1!=0:
		ans=abs(count0-count1)//2
		print(ans)
	else:
		print(-1)
# for _ in range(int(input())):
#     n = input()


#     p = len(n)

#     if p%2 == 1:
#         print(-1)
#     else:
#         o,z = 0,0
#         for i in n:
#             if i == '1':
#                 o +=1
#             else:
#                 z += 1
#         if o == z:
#             print(0)
#         elif o*z == 0:
#             print(-1)
#         else:
#             req = p//2
#             print(req-min(o,z))


