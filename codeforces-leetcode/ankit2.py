import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
import queue  
def minEdgeBFS(edges,u,v, n):  
    visited = [0] * n   
    distance = [0] * n   
    Q = queue.Queue() 
    distance[u] = 0
  
    Q.put(u)  
    visited[u] = True
    while (not Q.empty()): 
        x = Q.get()  
          
        for i in range(len(edges[x])): 
            if (visited[edges[x][i]]): 
                continue 
            distance[edges[x][i]] = distance[x] + 1
            Q.put(edges[x][i])  
            visited[edges[x][i]] = 1
    return distance[v]-1
def addEdge(edges, l, m): 
    edges[l].append(m)  
    edges[m].append(l)
    print(edges)
input1=int(input())
input2=int(input())
edges = [[] for i in range(input1+1)]
for _ in range(input2):
	x,y=map(int,input().split())
	addEdge(edges,x,y)
u=int(input())
v=int(input())
print(minEdgeBFS(edges, u, v, input1+1))

