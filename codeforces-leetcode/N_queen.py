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
# Step 1: Create set for all the three types of attacks Two diagonals and One Vertical attacks
# Step2: First diagonal is calculated by i+j and second diagonal j-i. If i+j or j-i is present in the set that means that particular diagonal is under attack.
# Step 3: If not under attack place the queen on board and add both the diagonals and vertical in the set which are under attack after placing that queen .
# Step 4: Now recurse for next row if at last we find that this solution is not valid we backtrack and pop all the value which we have filled earlier as that solution is not valid now and place the queen in next column in next iteration.
# Step 5: After finding solution just add that configuration of board into new list and return it.
# Thank You
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        diag1 = set()
        diag2 = set()
        vertical = set()
        i = 0
        board = [["." for j in range(n)]for i in range(n)]
        # print(board)
        def placeQueen(board,i,diag1,diag2,vertical):
            if i == len(board):
                addtoList(board)
                return;
            for j in range(n):
                if (i+j) not in diag1 and (j-i) not in diag2 and j not in vertical:
                    board[i][j] = 1
                    diag1.add(i+j)
                    diag2.add(j-i)
                    vertical.add(j)
                    if placeQueen(board,i+1,diag1,diag2,vertical):
                        return True
                    else:
                        board[i][j] = 0
                        diag1.remove(i+j)
                        diag2.remove(j-i)
                        vertical.remove(j)
        def addtoList(board):
            l = []
            for i in range(n):
                temp= ""
                for j in range(n):
                    if board[i][j] == 1:
                        temp += "Q"
                    else:
                        temp += "."
                l.append(temp)
            res.append(l)
                
        placeQueen(board,i,diag1,diag2,vertical)
        return res