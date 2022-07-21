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
	n = II()
	a = LI()
	b = sorted(set(a))
	b_ = set(a)
	# print(b_)
	for i in a:
		if i in b_:
			b_.remove(i)
		else:
			b.append(i)
	print(*b)
