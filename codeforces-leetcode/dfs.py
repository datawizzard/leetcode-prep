import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
from collections  import defaultdict
def dfs(adj_list,u):
	visited[u]="G"
	dfs_traversal.append(u)
	for v in adj_list[u]:
		if visited[v]=="W":
			parent[v]=u
			level[v]=level[u]+1
			dfs(adj_list,v)
	visited[u]="B"
	return dfs_traversal
n,m,u=map(int,input().split())
a =[list(map(int, input().split())) for i in range(n)]
adj_list = defaultdict(list)
for i in range(n):
	for j in range(m):
		if a[i][j]==1:
			adj_list[i].append(j)
visited={}
parent={}
level={}
dfs_traversal=[]
for node in adj_list.keys():
	visited[node]="W"
	parent[node]=None
	level[u]=0
print(dfs(adj_list,u))
print(level)
