import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
t = int(input())
for i in range(t):
    n = int(input())
    adjacent = [[] for i in range(n)]
    for i in range(n-1):
        u,v = map(int,input().split())
        adjacent[u-1].append(v-1)
        adjacent[v-1].append(u-1)
    v= [False]*n    
    ans = [0]*n
    ans[0] = 1 
    from collections import deque
    stack = deque()
    stack.append(0)
    len_ = 1
    while len_!=0:
        temp = stack.popleft()
        v[temp] = True
        len_-=1
        for i in adjacent[temp]:
            if not v[i]:
                stack.append(i)
                len_+=1
                if ans[temp] == 1:
                    ans[i] = 2
                else:
                    ans[i] = 1 
    print(*ans)                