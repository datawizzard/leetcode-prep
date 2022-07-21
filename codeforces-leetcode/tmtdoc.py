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
from collections import Counter
for _ in range(II()):
	n = II()
	s = I()
	c = Counter(s)
	# print(c)
	a,b,flag= 0,0,0
	if c['T'] != 2*c['M']:
		print('NO')
		continue;
	else:
		for i in range(n):
			if s[i] == 'T':
				a += 1
			elif s[i] == 'M':
				b += 1
			if b > a:
				flag = 1
				break;
	if flag == 1:
		print("NO")
		continue
	else:
		a,b,flag = 0,0,0
		s = s[::-1]
		# print(s)
		for i in range(n):
			if s[i] == 'T':
				a += 1
			elif s[i] == 'M':
				b += 1
			if b > a:
				flag = 1
				break;
	if flag == 1:
		print("NO")
	else:
		print("YES")
