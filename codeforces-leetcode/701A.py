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
	a,b = MI()
	ans = 1e9
	for j in range(0,32):
		c = 0
		aa = a
		bb = b + j
		if bb == 1:
			continue;
		while aa > 0:
			aa //= bb
			c += 1
		ans = min(ans,c + j)
	print(ans)


