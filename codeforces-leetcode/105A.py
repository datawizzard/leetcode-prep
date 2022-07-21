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
def isbalanced(x):
	c = 0
	for i in range(len(s)):
		if x[i] == "(":
			c += 1
		if x[i] == ")":
			c -= 1
		if c < 0:
			return False
		if i == len(s) - 1 and c != 0:
			return False
	return True
for _ in range(II()):
	s = I()
	a = ""
	b = ""
	x = s[0]
	y = s[len(s)-1]
	for i in range(len(s)):
		if s[i] == x:
			a += "("
		elif s[i] == y:
			a += ")"
		else:
			a += ")"
	for i in range(len(s)):
		if s[i] == x:
			b += "("
		elif s[i] == y:
			b += ")"
		else:
			b += "("
	# print(a)
	# print(b)
	if (isbalanced(a) == True) or (isbalanced(b) == True):
		print("YES")
	else:
		print("NO")

	

