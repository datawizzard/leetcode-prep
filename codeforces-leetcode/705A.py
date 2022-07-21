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
	a = []
	if n == 1:
		print(0)
	else:
		l = (k + 1)// 2
		for i in range(l,n+1):
			if i != k:
				a.append(i)
		print(len(a))
		print(*a)

		