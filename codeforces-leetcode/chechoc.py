import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
for _ in range(int(input())):
	n,m,x,y=map(int,input().split())
	p=(n*m)
	if p==1:
		ans=x
	elif y//2>=x:
		print((n*m)*x)
	elif y>=x:
		if p%2==0:
			print(p//2*y)
		else:
			print((p//2)*y+x)
	else:
		print(((n*m+1)//2)*y)

