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
	mini = 9999
	k = II()
	for i in range(1,101):
		for j in range(101):
			if (i * 100)/(i+j) == k:
				# print(i,j)
				mini = min(mini,i+j)
	print(mini)