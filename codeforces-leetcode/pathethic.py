import sys
import queue 
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
for _ in range(int(input())):
	n=int(input())
	v=[[] for i in range(n+1)]
	for i in range(n-1):
		f,s=map(int,input().split())
		v[f].append(s)
		v[s].append(f)
	print(v)
	level=[0]*(n+1)
	level[0]=0
	level[1]=1
	visited=[0]*(n+1)
	q=[]
	q.append(1)
	while(len(q)>0):
		x=q[-1]
		q.pop()
		visited[x]=1
		j=0
		while(j<len(v[x])):
			if(visited[v[x][j]]==False):
				level[v[x][j]]=level[x]+1
				q.append(v[x][j])
				print(level)
				print(q)
			j+=1
	ans=[0]*(n+1)
	ans[0]=0
	ans[1]=1
	print("1")
	for i in range(2,n+1):
		ans[i]=(2*level[i]-1)*(2*level[i]-2);
		print(ans[i])
	print()
