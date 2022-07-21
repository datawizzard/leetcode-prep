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
	n,x = MI()
	w = LI()
	s ,flag = 0,0
	w.sort()
	b = []
	a = []
	if sum(w) == x:
		print("NO")
	else:
		for i in range(n):
			if s + w[i] == x:
				b.append(w[i])
			else:
				a.append(w[i])
				s += w[i]
		# print(w)
		# print(b)
		# for i in range(len(b)):
		# 	if s + b[i] == x:
		# 		flag = 1
		# 	else:
		# 		s += b[i]

		# if flag == 1:
		# 	print("NO")
		# else:
		print("YES")
		a.extend(b)
		print(*a)
