
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
def res(matrix,n):   
    new_m =[]
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == '*':
                new_m.append([i,j])
    a,c = new_m[0][0],new_m[0][1]
    b,d = new_m[1][0],new_m[1][1]
    res = [['.']*n for i in range(n)] 
    res[a][c] = '*'
    res[b][d] = '*'
    res[a][d] = '*'
    res[b][c] = '*' 
    if a == b and a != n-1 :
        res[a+1][c],res[b+1][d] = "*","*"
    elif a == b and a == n-1 :
        res[a-1][c],res[b-1][d] = "*","*"
    elif c == d and c != n-1 :
        res[a][c+1],res[b][d+1] = "*","*"
    elif c == d and c == n-1 :
        res[a][c-1],res[b][d-1] = "*","*" 
    for i in range(n):
        for j in range(n): 
            print(res[i][j],end ="")
        print() 
for _ in range(II()):
    n = II()
    matrix = []
    for i in range(n):
        a = list(input())
        matrix.append(a) 
    res(matrix,n)