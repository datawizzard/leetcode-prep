import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
for _ in range(int(input())):
	n=int(input())
	res=list(map(int,input().split()))
	own=list(map(int,input().split()))
	c=[(i,j) for i,j in zip(res,own)]
	c.sort(reverse=True)
	print(c)
	z = 0
	for i in range(n):
		x, y = c[i]
		print(x,y)
		if x > y and y + z < x:
			z += y
		else:
			z = max(z, x)
			break
	print(z)
		



