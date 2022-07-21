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
	X,R,M = MI()
	R = R * 60
	M = M * 60
	req = 0
	req += min(X,R)
	R -= req
	req += 2*R
	if req <= M:
		print("YES")
	else:
		print("NO")