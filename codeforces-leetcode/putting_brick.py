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
	n=int(input())
	arr = [[j for j in I()] for i in range(n)]
	a=arr[0][1]
	b=arr[1][0]
	c=arr[n-1][n-2]
	d=arr[n-2][n-1]
	if a==b and c==d:
		if a!=c:
			print(0)
		else:
			print(2)
			print(n,n-1)
			print(n-1,n)
	elif a == d and b == c:
		print(2)
		print(1,2)
		print(n,n-1)
	elif a == c and b == d and a != b:
		print(2)
		print(1,2)
		print(n-1,n)
	elif a == b and c != d:
		if c == a:
		    print(1)
		    print(n,n-1)
		elif d == a:
		    print(1)
		    print(n-1,n)
	elif c == d and a != b:
		if a == c:  
		    print(1)
		    print(1,2)
		elif c == b:
		    print(1)
		    print(2,1)

