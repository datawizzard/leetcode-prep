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
def isPerfectSquare(x): return (int(math.sqrt(x))*int(math.sqrt(x)) == x)

for _ in range(II()):
	x = II()
	if x % 2 == 0:
		if isPerfectSquare(x) or (isPerfectSquare(x//2)):
			print("YES")
		else:
			print("NO")
	else:
		print("NO")