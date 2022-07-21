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
from queue import Queue
n = II()
path = [[] for i in range(n)]
visited = [0]*n
que = Queue()
bfs = []
for _ in range(n - 1):
	a,b = MI()
	path[a].append(b)
	path[b].append(a)
print(path)
for i in range(n):
	if visited[i] == 0:
		que.put(i)
		visited[i] = 1
		while que.empty() == False:
			x = que.get()
			bfs.append(x + 1)
			for l in path[x]:
				print(l)
				if visited[l] == 0:
					visited[l] = 1
					que.put(l)
print(bfs)

