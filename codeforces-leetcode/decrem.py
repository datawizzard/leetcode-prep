import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
for _ in range(int(input())):
	l,r=map(int,input().split())
	if 2*l<=r or l==1:
		print(-1)
	else:
		print(r)
