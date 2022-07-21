import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
from collections import deque
n=int(input())
y=[500]*(100001)
y[100000]=0
ans=0
for i in range(n):
    temp1,temp2=list(map(int,input().split()))
    if temp2<y[temp1]:
        y[temp1]=temp2
stack=deque()
for i in range(1,100001):
    while (len(stack)!=0) and (y[stack[-1]]>y[i]):
        h=y[stack.pop()]
        j=0 
        if len(stack)!=0:
            j=stack[-1]
        ans=max(ans,(i-j)*h)
    stack.append(i)
print(ans)
