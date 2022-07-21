# import sys
# sys.stdin=open('input.txt','r')
# sys.stdout=open('output.txt','w')
import sys
import math
import heapq
def input(): return sys.stdin.readline().strip("\n")
def I():    return (input())
def II():    return (int(input()))
def MI():    return (map(int,input().split()))
def LI():    return (list(map(int,input().split())))
def isPerfectSquare(x): return (int(math.sqrt(x))**2 == x)
for _ in range(II()):
	s1,s2,s3,s4 = MI()
	a = [s1,s2,s3,s4]
	k = a[:]
	a.sort()
	maxi = a[-1]
	secondmax = a[-2]
	l = max(k[0],k[1])
	m = max(k[2],k[3])
	# print(l,m,maxi,secondmax)
	if (l,m) == (maxi,secondmax) or (m,l) == (maxi,secondmax):
		print("YES")
	else:
		print("NO")
