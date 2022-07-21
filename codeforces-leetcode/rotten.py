import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
class Solution:
    def orangesRotting(self, grid):
       
        fresh = set()
        rotton = set()
        
        m = len(grid)
        n = len(grid[0])
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    rotton.add((i,j))
                elif grid[i][j] == 1:
                    fresh.add((i, j))
        # print(rotton)
        # print(fresh)            
        mins = 0
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        
        while len(fresh) > 0:
            infected = set()
            
            for r in rotton:
                
                row = r[0]
                col = r[1]

                for dir in dirs:
                    new_row = dir[0] + row
                    new_col = dir[1] + col
                    
                    if (new_row, new_col) in fresh:
                        fresh.remove((new_row, new_col))
                        infected.add((new_row, new_col))
                        # print(fresh,"fresh")
                        # print(infected,"infected")
            if len(infected) == 0:
                return -1
            
            rotton = infected
            # print(rotton,"rotton")
            mins += 1
            
        return mins
n,m=map(int,input().split())
a =[list(map(int, input().split())) for i in range(n)]
#print(a)
x=Solution()
print(x.orangesRotting(a))
