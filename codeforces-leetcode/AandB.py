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
for _ in range(II()):
	a,b = MI()
	c = min(a,b)
	d = max(a,b)
	i,res = 1,0
	while c != d:
		if d - c > 1:
			c += i
			i += 1
			res += 1
		else:
			d += i
			i += 1
			res += 1
		if c == d:
			break;
	print(res)


