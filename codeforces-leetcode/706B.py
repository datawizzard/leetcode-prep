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
	n,k = MI()
	a = LI()
	a = set(a)
	while k > 0:
		a.sort()
		j = 1
		for i in a:
			if j  not in a:
				mex = j + 1
				break;
			j += 1
		maxi = max(a)
		# print(maxi,mex)
		s.add((mex+maxi)//2)
		k -= 1
	print(len(set(s)),*s)
	

	