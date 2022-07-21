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
def wordsearch(board,word):
	m = len(board)
	n = len(board[0])
	def dfs(i,j,count,word):
		if i < 0 or j <0 or i >= m or j >= n or board[i][j] != word[count]:
			return False
		# In question it is mentioned same letter in grid cannot be used more than once
		# for tackling this we have change it after the use of that letter so that it cannot 
		# be matched with any other word again and after recursion completes we have to put it back
		temp = board[i][j]
		board[i][j] = "."
		found = (dfs(i+1,j,count + 1,word) or
				dfs(i-1,j,count + 1,word) or
				dfs(i,j+1,count + 1,word) or
				dfs(i,j-1,count + 1,word))
		board[i][j] = temp
		return found
	for i in range(m):
		for j in range(n):
			if board[i][j] == word[0] and dfs(i,j,0,word):
				return True
	return False