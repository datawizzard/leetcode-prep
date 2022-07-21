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
for _ in range(II()):
 	matrix = []
    for i in range(n):
        a = list(input())
        matrix.append(a)
    def isValid(board, row, col, num):
            for x in range(9):
                if board[row][x] == num:
                    return False
            for x in range(9):
                if board[x][col] == num:
                    return False
            startRow = row // 3 * 3
            startCol = col // 3 * 3
            for i in range(3):
                for j in range(3):
                    if board[i + startRow][j + startCol] == num:
                        return False
            return True
        def solve(board,i,j):
            if i == 9:
                return True
            if j == 9:
                return solve(board,i+1,0)
            if board[i][j] == ".":
                for num in range(1,10):
                    num = str(num)
                    if isValid(board,i,j,num) == True:
                        board[i][j] = num
                        if solve(board,i,j+1):
                            return True
                        else:
                            board[i][j] = "."
            else:
                return solve(board,i,j+1)
        solve(board,0,0)
