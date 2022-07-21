import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
from itertools import permutations 
for _ in range(int(input())):
	n=int(input())
	s=input()
	t=input()
	if s==t:
		print("EQUAL")
	else:
		# a=[''.join(l) for l in permutations(s)]
		# b=[''.join(m) for m in permutations(t)]
		# # print(a)
		# # print(b)
		# c=0
		# c1=0
		# for i,j in zip(a,b):
		# 	if i>j:
		# 		c+=1
		# 	else:
		# 		c1+=1
		# print(c,c1)
		# if c>c1:
		# 	print("RED")
		# elif c<c1:
		# 	print("BLUE")
		# else:
		# 	print("EQUAL")
		p=list(s)
		q=list(t)
		c,c1=0,0
		for i,j in zip(p,q):
			if i>j:
				c+=1
			elif i<j:
				c1+=1
		# print(c,c1)
		if c>c1:
			print("RED")
		elif c<c1:
			print("BLUE")
		else:
			print("EQUAL")
		