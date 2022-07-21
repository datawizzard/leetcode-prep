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
	n = II()
	c = 0
	if n % 2050 != 0:
		print(-1)
	else:
		q = n // 2050
		q = str(q)
		# print(q)
		a = list(map(int,q))
		print(sum(a))
