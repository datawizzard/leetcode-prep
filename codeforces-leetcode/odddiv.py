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
def isPowerOfTwo (x):
    return (x and (not(x & (x - 1))))
for _ in range(II()):
	n = II()
	if n%2 == 1:
		print("YES")
	else:
		if isPowerOfTwo(n) == True:
			print("NO")
		else:
			print("YES")
