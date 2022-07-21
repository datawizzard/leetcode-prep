import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
import sys
import math
import heapq
def input(): return sys.stdin.readline().strip("\n")
def I():    return (input())
def II():    return (int(input()))
def MI():    return (map(int,input().split()))
def LI():    return (list(map(int,input().split())))
def isPerfectSquare(x): return (int(math.sqrt(x))**2 == x)
def dfs(i,visited,path,dfsarr):
	dfsarr.append(i + 1)
	visited[i] = 1
	for l in path[i]:
		if visited[l] == 0:
			dfs(l,visited,path,dfsarr)
n = II()
path = [[] for i in range(n)]
visited = [0]*n
dfsarr = []
for _ in range(n - 1):
	a,b = MI()
	path[a].append(b)
	path[b].append(a)
print(path)
for i in range(n):
	if visited[i] == 0:
		dfs(i,visited,path,dfsarr)
print(dfsarr)