import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
t=int(input())
for _ in range(t):
	n,x=map(int,input().split())
	a=list(map(int,input().split()))
	b=list(map(int,input().split()))
	a.sort()
	b.sort(reverse=True)
	ans="Yes"
	for i, j in zip(a,b):
		if i+j>x:
			ans="No"
			break;
		else:
			ans="Yes"
	print(ans)
	if _<t-1:
		input()
		
