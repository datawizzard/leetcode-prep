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
	h = LI()
	x = [0]*n
	s = 0
	for i in range(n):
		x[i] = i
	# print(x)
	for i in range(n):
		s += h[i] - x[i]
		if s < 0:
			print("NO")
			break;
	else:
		print("YES")