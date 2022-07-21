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
# a
for _ in range(II()):
	n = II()
	b = I()
	r=['1']
	for i in range(1,n):
		x = int(b[i-1])
		y = int(r[i-1])
		s = x + y
		if s == 2:
			if b[i] == '1':
				r.append('0')
			elif b[i] == '0':
				r.append('1')
		elif s == 1:
			if b[i] == '1':
				r.append('1')
			elif b[i] == '0':
				r.append('0')
		elif s == 0:
			r.append('1')
	print("".join(r))
