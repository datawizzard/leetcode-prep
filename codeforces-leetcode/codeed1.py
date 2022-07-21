import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
for _ in range(int(input())):
    n,m = map(int,input().split())

    a,g =[[0]*(m+1) for i in range(n+1)],[0]*(n+1)
    
    for i in range(n):
        g[i] =list(map(int,input().split()))


    f = 0
    
    #print(a,g)    
    
    for i in range(n+1):
        for j in range(m+1):
            if (i == 0 and j==0) or (i==0 and j==m) or (i==n and j==0) or (i==n and j==m):
                a[i][j] = 2
            elif i > 0 and j == 0 and i< n:
                a[i][j] = 3
            elif j > 0 and i==0 and j<m:
                a[i][j] = 3
            elif i>0 and j==m and i<n:
                a[i][j] = 3
            elif j >0 and i==n and j<m:
                a[i][j] = 3
            else:
                a[i][j] = 4
            print(i,j)
            print(a)


    i,j = 0,0
    for i in range(n):
        for j in range(m):
            if g[i][j] > a[i][j]:
                #print('No')
                f = 1
                break
    if f == 1:
        print('No')
    else:
        print('Yes')
        for p in range(n):
            print(*a[p])