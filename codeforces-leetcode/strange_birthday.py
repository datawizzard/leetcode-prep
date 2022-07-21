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
	n,m=MI()
	a=LI()
	b=LI()
	a.sort(reverse=True)
	# print(a)
	s,j=0,0
	for i in a:
		if j<i:
		    s+=b[j]
		    j+=1
		    # print(s,j)
		else:
			s+=b[i-1]
			# print(s)
	print(s)
