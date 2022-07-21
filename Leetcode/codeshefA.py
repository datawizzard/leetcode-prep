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
n = int(input())
board = [[x for x in input()] for _ in range(n)]
words = input()
def searchWord(board, words):
	def bogglewords(board,m,n,words,res,visited,path):
		for i in range(m):
		    for j in range(n):
		        if board[i][j] == words[0]:
		            dfs(i,j,m,n,board,words,visited,path)
		            return [[i,j]]
	def dfs(i,j,m,n,board,words,visited,path):
	    direction = [[-1,0],[0,-1],[1,0],[0,1]]
	    visited[i][j] = True 
	    path += board[i][j]
	    if path == words:
	        res.add(path)
	    for x,y in direction:
	        new_x = x + i 
	        new_y = y + j
	        if new_x < 0 or new_y < 0 or new_x >= m or new_y >= n or visited[new_x][new_y] == True:
	            continue;
	        dfs(new_x,new_y,m,n,board,words,visited,path)
	    visited[i][j] = False
	m = len(board)
	n = len(board[0])
	visited = [[False for j in range(n)]for i in range(m)]
	res = set()
	return bogglewords(board,m,n,words,res,visited,"")
print(searchWord(board,words))

