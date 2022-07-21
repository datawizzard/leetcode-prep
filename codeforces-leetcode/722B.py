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
	n = II()
	s = I()
	zero = 0
	for i in range(n):
		if s[i] == '0':
			zero += 1
	if s[n//2] == '0' and zero % 2 == 1 and zero > 1:
		print("ALICE")
	else:
		print("BOB")