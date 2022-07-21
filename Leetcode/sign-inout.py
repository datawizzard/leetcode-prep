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
from collections import defaultdict
arr = LI()
d = II()
result= []
for i in range(len(arr)):
    if i == 0:
        s = 1
    else:
        s = arr[i-1] + 1
    if i != len(arr):
        e = arr[i]
    else:
        e = float('inf')
    if d < s:
        break;
    for k in range(s,e):
        if k <= d:
            result.append(k)
            d -= k
        else:
            break;
print(result)


# Balance Parenthesis
bal=0
ans=0
for i in range(0,len(p)):
	if(p[i]=='('):
		bal+=1
	else:
		bal+=-1
		
	# It is guaranteed bal >= -1
	if(bal==-1):
		ans+=1
		bal+=1
return bal+ans