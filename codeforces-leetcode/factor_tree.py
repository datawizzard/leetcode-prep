import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
def addEdge(x,y,v):
	v[x].append(y)
	v[y].append(x)
for _ in range(int(input())):
	n=int(input())
	v=[[] for i in range(n+1)]
	for _ in range(n-1):
		x,y=map(int,input().split())
		addEdge(x,y,v)
	arr=list(map(int,input().split()))
	q=int(input())
	for _ in range(q):
		u,v=map(int,input().split())
		stack=[]
	


