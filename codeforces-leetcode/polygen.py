import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
for _ in range(int(input())):
	n=int(input())
	ans=0
	for _ in range(n):
		x,y=map(int,input().split())
		while(n>=3):
			ans+=n
			n=n//2
	print(ans)

