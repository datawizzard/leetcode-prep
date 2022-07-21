import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
import sys
import math
import heapq
def input(): return sys.stdin.readline().strip("\n")
def I():    return (input())
def II():    return (int(input()))
def MI():    return (map(int,input().split()))
def LI():    return (list(map(int,input().split())))
def isPerfectSquare(x): return (int(math.sqrt(x))**2 == x)
a = int(input())
b = int(input())
if len(str(a)) < len(str(b)):
	print("NO")
else:
	while b > 0:
		if b % 10 != a % 10:
			print("NO")
			break;
		b = b //10
		a = a//10
	else:
		print("YES")