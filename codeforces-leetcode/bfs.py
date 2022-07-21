import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
from collections  import defaultdict
from queue import Queue
def queu(adj_list,s):
	visited={}
	level={}
	parent={}
	bfs_traversal=[]
	queue=Queue()
	for node in adj_list.keys():
		visited[node]=False
		parent[node]=None
		level[node]=-1
	visited[s]=True
	level[s]=0
	queue.put(s)
	while not queue.empty():
		u=queue.get()
		bfs_traversal.append(u)
		for v in adj_list[u]:
			if not visited[v]:
				visited[v]=True
				parent[v]=u
				level[v]=level[u]+1
				queue.put(v)
	print(bfs_traversal)
	#shortest distance from all source node
	print(level)
	#shotest path from any node to source node here v is destination node
	v=3
	path=[]
	while v is not None:
		path.append(v)
		v=parent[v]
	path.reverse()
	print(*path)

n,m,s=map(int,input().split())
a =[list(map(int, input().split())) for i in range(n)]
adj_list = defaultdict(list)
for i in range(n):
	for j in range(m):
		if a[i][j]==1:
			adj_list[i].append(j)
queu(adj_list,s)

