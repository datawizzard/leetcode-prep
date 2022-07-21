import sys
import math
def input(): return sys.stdin.readline().strip("\n")
def I():    return (input())
def II():    return (int(input()))
def MI():    return (map(int,input().split()))
def LI():    return (list(map(int,input().split())))
from bisect import bisect_left
n,q = MI()
a = LI()
b = LI()
for i in b:
	c = a.index(i)
	print(c + 1,end = " ")
	a[:c+1]=[i]+a[:c]


