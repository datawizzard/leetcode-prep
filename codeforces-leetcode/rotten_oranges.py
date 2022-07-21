import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
class Solution:
    def orangesRotting(self, grid):
        def rotting(rotten):
            temp = []
            for i, j in rotten:
                # top
                if i > 0 and grid[i - 1][j] == 1:
                    temp.append((i-1,j))
                    grid[i-1][j] = 2
                #bottom
                if i <n-1 and grid[i + 1][j] == 1:
                    temp.append((i+1,j))
                    grid[i+1][j] = 2
                #left
                if j > 0 and grid[i][j - 1] == 1:
                    temp.append((i,j-1))
                    grid[i][j-1] = 2
                # right
                if j <m-1 and grid[i][j + 1] == 1:
                    temp.append((i,j+1))
                    grid[i][j + 1] = 2
            return temp

        rotten = [(i,j) for i in range(n) for j in range(m) if grid[i][j] == 2]
        count = 0
        while len(rotten)!=0:
            rotten=rotting(rotten)
            print(rotten)
            if len(rotten) == 0:
                break
            count += 1
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    return -1    
        return count
n,m=map(int,input().split())
a =[list(map(int, input().split())) for i in range(n)]
#print(a)
x=Solution()
print(x.orangesRotting(a))