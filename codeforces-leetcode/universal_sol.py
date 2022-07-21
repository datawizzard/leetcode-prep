# import sys
# sys.stdin=open('input.txt','r')
# sys.stdout=open('output.txt','w')
import sys
import math
from collections import Counter
def input(): return sys.stdin.readline().strip("\n")
def I():    return (input())
def II():    return (int(input()))
def MI():    return (map(int,input().split()))
def LI():    return (list(map(int,input().split())))
for _ in range(II()):
	s = I()
	a = Counter(s)
	# print(a)
	r = a.most_common(1)[0][0]
	if r == 'R':
		print('P'*len(s))
	elif r == 'P':
		print('S'*len(s))
	else:
		print('R'*len(s))