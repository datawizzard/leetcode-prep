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

for _ in range(int(input())):
	n,k=map(int,input().split())
	arr=list(map(str,input().split(" ")))
	arr=arr[::-1]
	# print(arr)
	for i in range(k):
		if arr[i]=='H':
			for j in range(i+1,n):
				if arr[j]=='H':
					arr[j]='T'
				elif arr[j]=='T':
					arr[j]='H'
	# print(arr)
	arr=arr[::-1]
	arr=arr[:n-k]
	print(arr)
	c=0
	for i in arr:
		if i == 'H':
			c+=1
	print(c)



