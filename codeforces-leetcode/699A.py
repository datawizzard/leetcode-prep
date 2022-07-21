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
	x,y = MI()
	s = I()
	u,d,r,l,px,py = 0,0,0,0,0,0
	u = s.count("U")
	d = s.count("D")
	r = s.count("R")
	l = s.count("L")
	# print(u,d,r,l)
	if x >= 0 and y >= 0:
		if r >= x and u >= y:
			print("YES")
		else:
			print("NO")
	elif x >= 0 and y <= 0:
		if r >= abs(x) and d >= abs(y):
			print("YES")
		else:
			print("NO")
	elif x <= 0 and y >= 0:
		if l >= abs(x) and u >= abs(y):
			print("YES")
		else:
			print("NO")
	elif x <= 0 and y <= 0:
		# print(l,d)
		if l >= abs(x) and d >= abs(y):
			print("YES")
		else:
			print("NO")
	# if x < 0:
	# 	px = abs(x)
	# if y < 0:
	# 	py = abs(y)
	# if px > 0 and l < px:
	#     print('NO')
	# elif y > 0 and u < y:
	#     print('NO')
	# elif py > 0 and d < py:
	#     print('NO')
	# elif x > 0 and r < x:
	#     print('NO')
	# else:
	#     print('YES')

