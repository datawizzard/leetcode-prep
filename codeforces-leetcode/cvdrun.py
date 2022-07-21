import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
for _ in range(int(input())):
	n,k,x,y=map(int,input().split())
	for i in range(n):
		if (x+k)%n==y:
			print("YES")
			break;
		else:
			x=(x+k)%n
	if i==n-1 and (x+k)%n!=y:
		print("NO")
