import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
import math
for _ in range(int(input())):
	a=input()
	b=input()
	c=len(a)
	d=len(b)
	e= math.gcd(len(a),len(b))
	lcm=(c*d)//e
	# print(e,lcm)
	if c==d and a!=b:
		print(-1)
	else:
		a=[a]*(lcm//c)
		a="".join(a)
		b=[b]*(lcm//d)
		b="".join(b)
		# print(a)
		# print(b)
		if a==b:
			print(a)
		else:
			print(-1)








