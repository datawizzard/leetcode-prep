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
# for _ in range(II()):
# 	a,b = MI()
# 	count = 0
# 	x = a*b
# 	y = a
# 	z = x + y
# 	p = a * b
# 	if z % p == 0:
# 		count += 1
# 	if x % p == 0:
# 		count += 1
# 	if y % p == 0:
# 		count += 1
# 	if count > 1:
# 		print("NO")
# 	else:
# 		print("YES")
# 		print(x,y,z)
for _ in range(II()):
	a,b = MI()
	z = a*b
	# if b == 1:
	# 	print("NO")
	if b == 2:
		print("YES")
		z = z * 2
		x = a*(2*b - 1)
		y = z - x
		print(x,y,z)
	elif b == 1:
		z = z * 3
		x = a*(3*b - 1)
		y = z - x
		print(x,y,z)
	else:
		print("YES")
		x = a*(b-1)
		y = a*b - x
		print(x,y,z)
