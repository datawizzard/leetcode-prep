import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
import math
for _ in range(int(input())):
    n,q = map(int,input().split())
    arr =input()
    for i in range(q):
        ans ="NO"
        l,r = map(int,input().split())
        for j in range(0,l-1):
            if arr[j] == arr[l-1]:
                ans ="YES"
                break
        for p in range(r,n):
            if arr[p] == arr[r-1]:
                ans ="YES"
                break
        print(ans)        
	




