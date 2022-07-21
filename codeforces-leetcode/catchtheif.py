import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
for _ in range(int(input())):
	x,y,k,n=map(int,input().split())
	p=min(x,y)
	q=max(x,y)
	while p<q:
		p+=k
		q-=k
	if p==q:
		print("Yes")
	else:
		print("No")
