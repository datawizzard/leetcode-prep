# import sys
# sys.stdin=open('input.txt','r')
# sys.stdout=open('output.txt','w')
import sys
import math
def input(): return sys.stdin.readline().strip("\n")
def I():    return (input())
def II():    return (int(input()))
def MI():    return (map(int,input().split()))
def LI():    return (list(map(int,input().split())))
n,q= MI()
ar = [[0]*n for i in range(2)]
cond = 0
for i in range(q):
    x,y = map(int,input().split())
    x -= 1
    y -= 1
    if ar[x][y] == 0:
        te = 1
    else:
        te = -1
    ar[x][y] = ar[x][y]^1
    # print(ar[x][y])
    for j in range(-1,2):
        if j + y >= 0 and y + j < n and ar[x^1][y+j] == 1:
            cond += te
    # print(cond)
    if cond==0:
        print('Yes')
    else:
        print('No')
        

    
    
        




	

