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
def ceilf(a,b):
	return int((a / b) + ((a % b) != 0))
for _ in range(II()):
	p,a,b,c = MI()
	x = ceilf(p,a)
	y = ceilf(p,b)
	z = ceilf(p,c)
	print(min(x*a,y*b,z*c) - p)