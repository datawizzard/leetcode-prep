import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
import sys
import math
def input(): return sys.stdin.readline().strip("\n")
def I():    return (input())
def II():    return (int(input()))
def MI():    return (map(int,input().split()))
def LI():    return (list(map(int,input().split())))
from collections import Counter
for _ in range(II()):
	n = II()
	a = LI()
	a.sort()
	s = a[0]
	p = a.count(s)
	print(n-p)
