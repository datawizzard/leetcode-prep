# import sys
# sys.stdin=open('input.txt','r')
# sys.stdout=open('output.txt','w')
import sys
import math
def input(): return sys.stdin.readline().strip("\n")
def I():    return (input())
def II():    return (int(input()))
def MI():    return (map(int,input().split()))
def LI():    return (list(map(int,input().split())))
for _ in range(II()):
	r,b,d = MI()
	x = abs(r-b)
	if x <= d or d >= math.ceil(x/min(r,b)):
		print("YES")
	else:
		print("NO")