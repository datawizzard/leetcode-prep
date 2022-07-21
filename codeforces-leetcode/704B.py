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
	p = LI()
	a = []
	m = 0
	for i,v in enumerate(p):
		# print(i,v)
		if m < v:
			a.append(i)
			m = v
	# print(a)
	b = []
	k = n
	for i in a[::-1]:
		b += p[i:k]
		k = i
	print(*b,sep=" ")
	
		
		





		


